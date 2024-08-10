meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "Sedikit ketidaksetujuan",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif/marah"
            }

print("Selamat datang di web kamus")
print("Masukkan hingga 5 kata yang ingin kamu ketahui!")

for i in range(5):
    word = input("\nKetik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

    if word == "END":
        print("\nTerima kasih telah menggunakan kamus")
        break
    
    if word in meme_dict.keys():
        # Apa yang harus kita lakukan jika kata itu ditemukan?
        print(meme_dict[word])
    else:
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
        print("\nMaaf, kata tidak ditemukan!")
