def yozish(fayl_ismi, matn):
    try:
        with open(fayl_ismi, 'w') as f:
            f.write(matn)
        print("Matn muvaffaqiyatli yozildi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

yozish("matn.txt", "Bu matn muvaffaqiyatli yozildi.")
