import random

# 1. Program Çıktısı
my_words = ["Hi!", "Python Pro", "Kodland"]
print(my_words[1])  # Çıktı: Python Pro

# 2. Kullanıcıdan Girdi Alma ve Yazdırma
name = input("İsminiz nedir? ")
print("Hi ", name)

# 3. Rastgele Emoji Seçimi
emojis = ["^^", "0_o", ":)", "¯\\_(ツ)_/¯", "(￢_￢)"]
print("Rastgele bir emoji: ", random.choice(emojis))

# 4. Kendim hakkında rastgele bir gerçek
facts = [
    "Ben bir Python meraklısıyım!",
    "En sevdiğim hobi fotoğraf çekmek.",
    "Bir zamanlar bir hackathon kazandım.",
    "Evde bir kedim var, adı Mırmır.",
    "En sevdiğim yemek sushi."
]

print("Kendim hakkında rastgele bir gerçek:")
print(random.choice(facts))

# 5. Sözlük Uygulaması
meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Agresifleşmek/sinirlenmek"
}

print("\nMeme Sözlüğü'ne hoş geldiniz!")
print("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!)")
print("Çıkmak için 'EXIT' yazın.")

while True:
    word = input("Kelime: ")
    if word == "EXIT":
        print("Sözlükten çıktınız.")
        break
    elif word in meme_dict:
        print(f"{word}: {meme_dict[word]}")
    else:
        print(f"Üzgünüm, '{word}' kelimesini bilmiyorum.")
