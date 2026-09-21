import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from openai import AsyncOpenAI

BOT_TOKEN = "8911767988:AAGI5rRmylJt0YnvBQiLncM48L5RsTwsu8w"
GROQ_API_KEY = "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"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

client = AsyncOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

@dp.message(F.text)
async def chat(message: Message):
    r = await client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": message.text}]
    )
    await message.answer(r.choices[0].message.content)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
