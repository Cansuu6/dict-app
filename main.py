meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "CREEPY" : "korkunç"
            }
            
meme1_dict = {
            "GOAT": "Tüm zamanlarin en iyisi",
            "YOLO": "bir kez hayata gelirsin",
            "AGGRO" : "agresifleşmek/sinirlenmek"
             }
            
print("Anlamlarını öğrenebileceğiniz kelimeler:", *meme_dict.keys(), *meme1_dict.keys())


for i in range(7):
    x = input("Hangi kelimenin anlamanı öğrenmek istersiniz?")
    x = x.upper()
    
    if x in meme_dict.keys():
        # Kelime eşleşiyorsa ne yapmalıyız?
        print(x, "kelimesinin anlamı: ", meme_dict[x])
        
    elif x in meme1_dict.keys():
        # Kelime eşleşiyorsa ne yapmalıyız?
        print(x, "kelimesinin anlamı: ", meme1_dict[x])
    else:
        # Kelime eşleşmiyorsa ne yapmalıyız?
        print("Maalesef yazdığınız kelime sözlükte bulunmamaktadır!")
