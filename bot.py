from telethon import TelegramClient, events
import requests
from datetime import datetime

api_id = 33297370
api_hash = "fbb78629e47a3f775e51235c1fb78dc3"
WEBHOOK  = "https://n.couponscopy.com/webhook/telegram" # ← غيّر
CHANNEL  = "@yt_add_bot" # ← غيّر

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=CHANNEL))
async def handler(event):
    text = event.message.message
    if not text:
        return

    payload = {
        "message": text,
        "channel": CHANNEL,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        r = requests.post(WEBHOOK, json=payload, timeout=10)
        print(f"✅ أُرسل | Status: {r.status_code}")
    except Exception as e:
        print(f"❌ خطأ: {e}")

client.start()
print("🤖 البوت يعمل ويراقب القناة...")
client.run_until_disconnected()
