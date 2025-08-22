Amžius = int(input("Įveskite savo amžių: "))

def patikrinti_amziu(amzius):
    if amzius < 18:
        print("Jūs esate nepilnametis.")
    elif 18<= amzius < 60:
        print("Jūs esate suaugęs.")
    else:
        print("Jūs esate pensininkas") 

patikrinti_amziu(Amžius)     


def patikrinti_lygybę(amzius):
    if amzius % 2 == 0:
        print("Jūsų amžius yra lyginis skaičius.")
    else:
        print("Jūsų amžius yra nelyginis skaičius.") 

patikrinti_lygybę(Amžius)           