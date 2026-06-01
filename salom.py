# ==============================================================================
#                 SBS-404: Kelajak Dasturlash Akademiyasi 🐍🚀
# ==============================================================================
# Ushbu fayl sizga Python dasturlash tilining go'zalligi va kuchini ko'rsatish
# uchun maxsus yaratildi. 
#
# Biz platformada to'liq brauzer ichida ishlovchi haqiqiy Python (WebAssembly)
# muhitini o'rnatdik! Uni sinab ko'rish uchun:
# 1. SBS-404 platformasidagi "Kod Muhiti" (Playground) bo'limiga o'ting.
# 2. O'ng tepa burchakdan "Python Muhiti 🐍" tugmasini bosing.
# 3. Yozilgan kodlarni "Kodni Ishga Tushirish" orqali brauzerning o'zida ishlating!
# ==============================================================================

import time

def tabrik_yo'lla(ism, daraja="Junior"):
    print("=" * 60)
    print(f"👋 Salom, {ism}! SBS-404 akademiyasiga xush kelibsiz!")
    print(f"⚡ Joriy darajangiz: {daraja} Developer")
    print("=" * 60)

def fibonachchi_generator(chegara):
    """
    Fibonachchi sonlar ketma-ketligini hisoblovchi generator.
    Bu xotirani tejash va professional dasturlashda juda qulay usul!
    """
    a, b = 0, 1
    count = 0
    while count < chegara:
        yield a
        a, b = b, a + b
        count += 1

# Dasturni ishga tushiramiz:
tabrik_yo'lla("Kiber Dasturchi", daraja="Full-Stack")

print("\n⚙️ Generator orqali dastlabki 10 ta Fibonachchi sonlarini hisoblamoqda...")
time.sleep(0.5)

sonlar_tarixi = list(fibonachchi_generator(10))
print(f"📊 Natija: {sonlar_tarixi}")

# Mavzular bo'yicha maslahat:
# AI Ustoziingiz bilan gaplashib, ushbu kodlarni brauzer ichida ham sinab ko'ring!
# SBS-404 AI Ustoz sizga Python-ning barcha sirlarini o'rgatadi.
