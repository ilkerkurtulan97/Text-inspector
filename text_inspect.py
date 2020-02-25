# Text inspector

# Author : Ilker Kurtulan



class Dosya():

    def __init__(self):

        # Enter your own text file name name
        with open("metin.txt","r",encoding = "utf-8") as file:

            dosya_icerigi = file.read()

            print(dosya_icerigi)

            kelimeler = dosya_icerigi.split()
            self.sade_kelimeler = list()



            for i in kelimeler:
                i = i.strip("\n")

                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.sade_kelimeler.append(i)

    def tum_kelimeler(self):

        kelimeler_kümesi = set()

        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)

        print("All words ..........................")

        for i in kelimeler_kümesi:

            print(i)

            print("*****************************")

    def kelime_frekansı(self):

        kelime_sozluk = dict()

        for i in self.sade_kelimeler:

            if(i in kelime_sozluk):
                kelime_sozluk[i] += 1
            else:
                kelime_sozluk[i] = 1

        for kelime,sayı in kelime_sozluk.items():

            print(" {} word repeated {} times ...........".format(kelime,sayı))

            print("----------------------------------------")






# Creating my object
dosya = Dosya()


# Calling my own function
dosya.kelime_frekansı()




