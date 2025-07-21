import datetime
import asyncio
import os
from telegram import Bot

# Ambil token dari environment
TOKEN = "7414062602:AAGGdBZqxRRONdaqRh7xe3VSab4xn39uE7c"
bot = Bot(token="7414062602:AAGGdBZqxRRONdaqRh7xe3VSab4xn39uE7c")

# === SETUP CONFIGURASI MANUAL ===
CHAT_ID = "-1002876426430"  # bisa ID grup/ID user
EVENT_NAME = "Launched Token TetrisChain"
EVENT_TIME = "2025-07-25 20:00:00"
CUSTOM_MESSAGE = ("🚨Launch in {jam} Hours {menit} Minutes {detik} Seconds. \n"
                  "⚡To The {event}.\n"
                  "🔥Stay Ready!. \n"
                  "🌐https://tetrischain.fun/")


# === Fungsi untuk hitung waktu tersisa ===
def get_countdown():
    event_dt = datetime.datetime.strptime(EVENT_TIME, "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()
    delta = event_dt - now

    if delta.total_seconds() <= 0:
        return None

    total_seconds = int(delta.total_seconds())
    jam = total_seconds // 3600
    menit = (total_seconds % 3600) // 60
    detik = total_seconds % 60
    return jam, menit, detik


# === Fungsi untuk kirim pesan setiap 15 menit ===
async def countdown_loop():
    while True:
        remaining = get_countdown()
        if remaining:
            jam, menit, detik = remaining
            msg = CUSTOM_MESSAGE.format(jam=jam,
                                        menit=menit,
                                        detik=detik,
                                        event=EVENT_NAME)
            await bot.send_message(chat_id=CHAT_ID, text=msg)
        else:
            await bot.send_message(chat_id=CHAT_ID,
                                   text=f"✅ {EVENT_NAME} sudah dimulai!")
            break
        await asyncio.sleep(300)  # 5 menit = 300 detik


# === Jalankan bot tanpa polling command ===
async def main():
    await countdown_loop()


if __name__ == "__main__":
    asyncio.run(main())
