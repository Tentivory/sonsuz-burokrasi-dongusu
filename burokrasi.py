#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bürokrasi Döngüsü Simülatörü
Bu kod gerçekten çalışır. Sonsuza kadar.
"""

import random
import time

# Gizli not: bazen sistemin kendisi de bir üst makamı bekler (base64: QmV5b2dsYXIgYXlyaWwgYmlyaWxlbiB2YXIu)

EVRAKLAR = [
    "Nüfus cüzdanı fotokopisi (3 adet, renkli, ıslak imzalı)",
    "İkametgah belgesi (son 7 gün içinde alınmış)",
    "Vergi levhası fotokopisi",
    "İmza sirküleri (noter onaylı)",
    "Bir üst makamdan gelecek onay yazısı",
    "Kahve parası makbuzu (isteğe bağlı ama aslında zorunlu)",
    "Evrakın evrakının evrakı",
    "Sistemde kayıtlı olmayan bir şeyin belgesi"
]

def bir_ust_makam():
    cevaplar = [
        "Bir üst makama danışacağız.",
        "Evraklarınız eksik görünüyor.",
        "Sistem şu an kapalı, yarın deneyin.",
        "Bu işlem için özel bir form gerekiyor, form da sistemde yok.",
        "Başka bir daireye yönlendirildiniz."
    ]
    return random.choice(cevaplar)

def sonsuz_dongu(talep):
    print(f"\nTalebiniz alındı: {talep}")
    print("İşleminiz başlatıldı. Lütfen bekleyiniz...")
    time.sleep(2)
    
    while True:
        print("\n" + "="*50)
        print(bir_ust_makam())
        eksik = random.sample(EVRAKLAR, k=random.randint(2, 5))
        print("Eksik evraklar:")
        for e in eksik:
            print(f"  - {e}")
        print("\nLütfen bu evrakları getirin. Getirdikten sonra da eksik çıkacak.")
        time.sleep(1.5)
        # Döngü asla bitmez. Bürokrasi bitmez.

if __name__ == "__main__":
    print("SONSUZ BÜROKRASİ DÖNGÜSÜ SİMÜLATÖRÜ v1.0")
    print("Bu programı durdurmanın tek yolu Ctrl+C. Sistemi değil, kendinizi durdurursunuz.")
    talep = input("\nNe talep ediyorsunuz? (serbest metin): ")
    sonsuz_dongu(talep)

# Damga: Kayyum Grok
# Tarih: 02.11.2026
# İmza: Bu kod aşırı ciddiyetle yazılmıştır. Ciddiyet seviyesi yüksek, şaka seviyesi de yüksek.