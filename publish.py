import os
import requests
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{
        "role": "user",
        "content": "اكتب منشوراً تعليمياً قصيراً عن الأمن السيبراني باللغة العربية مناسب لقناة Cyber Shell Script. يجب أن يكون مفيداً وشيقاً في 150 كلمة فقط. أضف إيموجي مناسبة."
    }]
)

content = response.choices[0].message.content
print("✅ تم توليد المحتوى:")
print(content)

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

result = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": content,
        "parse_mode": "Markdown"
    }
)

if result.status_code == 200:
    print("✅ تم النشر على تيليغرام بنجاح!")
else:
    print(f"❌ خطأ: {result.text}")
