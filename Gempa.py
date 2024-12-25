class Gempa:
    def __init__(self, skala, lokasi):
        self.skala = skala
        self.lokasi = lokasi

    def dampak (self):

        print(f"ada gempa baru nich di {self.lokasi}")
        print(f"skala dari gempa ini adalah {self.skala}")
        if self.skala < 2:
            print('dampak ga berasa')
        elif self.skala >= 2 and self.skala <=4:
            print('dampak gempa bangunan retak-retak')
        elif self.skala >= 4 and self.skala <=6:
            print('dampak gempa bangunan roboh')
        elif self.skala > 6:
            print('dampak gempa bangunan roboh dan berpotensi tsunami')
        else:
            print('sistem tidak dapat membaca')






#Gempa ().skala = 2
#Gempa().dampak ()

#gempa1 = Gempa(5, "Cianjur")
#gempa1.dampak ()

