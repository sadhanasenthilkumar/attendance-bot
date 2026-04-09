import requests
from telegram import Bot
import asyncio

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

LOGIN_URL = "https://ims.ritchennai.edu.in/login"

async def send_attendance():
    session = requests.Session()

    # login (you may need to adjust fields)
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    session.post(LOGIN_URL, data=payload)

    # open attendance page (adjust URL if needed)
    attendance_url = "https://ims.ritchennai.edu.in/attendance"

    response = session.get(attendance_url)

    with open("attendance.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="📊 Attendance fetched successfully (check HTML manually)"
    )

asyncio.run(send_attendance())
