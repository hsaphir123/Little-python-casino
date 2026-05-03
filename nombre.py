import random
def charger_solde():
    try:
        with open("save.txt", "r") as fichier:
            return int(fichier.read())
    except (FileNotFoundError, ValueError):
        return 100
def sauvegarder_solde(solde):
    with open("save.txt", "w") as fichier:
        fichier.write(str(solde))
def jouer_nombre(solde):
    """Jeu de devinette de nombre"""
    print(f"\n=== JEU DU NOMBRE ===")
    print(f"Vous avez {solde}$")
    mise = int(input("Ta mise? "))
    if mise > solde:
        print("tu peut pas faire ça")
        return solde

    confirmation = input(f"Confirmer la mise de {mise}$ ? (Y/N) : ")
    if confirmation.upper() == "Y":
        solde -= mise
        print("Choisir un nombre de 1 a 10 (vous avez 3 essai)")

        hide_number = random.randint(1, 10)

        for i in range(3):
            essai = int(input(f"Essai {i+1}/3 - Ton choix : "))
            if essai == hide_number:
                nombre_bonus = int(mise * 2.5)
                print(f"GG tu vien de gagner {nombre_bonus}$")
                solde += nombre_bonus + mise
                break
            else:
                print("faux essaie encore")
        else:
            print(f"Perdu! Le nombre était {hide_number}")
    else:
        print("mise annulée")
    
    return solde

def jouer_roulette(solde):
    """Jeu de roulette"""
    print(f"\n=== JEU DE ROULETTE ===")
    print(f"Vous avez {solde}$")
    mise = int(input("Ta mise? "))
    if mise > solde:
        print("tu peut pas faire ça")
        return solde

    confirmation = input(f"Confirmer la mise de {mise}$ ? (Y/N) : ")
    if confirmation.upper() == "Y":
        solde -= mise
        result_roulette = random.choice(["rouge", "noir"])
        
        choix = input("Rouge ou noir? ").lower()
        print(f"La roulette tourne... {result_roulette}")
        
        
        if choix == result_roulette:
            roulette_bonus = mise * 2
            print(f"GG tu vien de gagner {roulette_bonus}$")
            solde += roulette_bonus + mise
        else:
            print(f"Perdu! C'était {result_roulette}")
    else:
        print("mise annulée")
    
    return solde

solde = charger_solde()
while True:
    print(f"\n--- Solde: {solde}$ ---")
    
    if solde == 0:
        print("Tu es ruiné!")
        if input("Tu veux essayer un autre jeu? (Y/N) ").upper() == "Y":
            pass
            solde += 25
        else:
            break
    
    print("\nQuel jeu voulez-vous jouer?")
    print("1. Nombre")
    print("2. Roulette")
    print("3. Quitter")
    
    choix = input("Ton choix (1/2/3): ")
    
    if choix == "1":
        solde = jouer_nombre(solde)
    elif choix == "2":
        solde = jouer_roulette(solde)
    elif choix == "3":
        sauvegarder_solde(solde)
        print(f"Au revoir! Solde final: {solde}$")
        break
    else:
        print("Choix invalide")