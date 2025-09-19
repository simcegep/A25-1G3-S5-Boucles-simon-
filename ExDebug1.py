def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"


if __name__ == "__main__":
    # TODO : demander le nombre d'ordi
    # TODO : créer 3 liste (tempertaure, poussiere et humidité)

    # TODO : pour le nombre d'oridinateur
    # TOdO : demander la temperature, poussiere et humidite [gestion d'erreur]
    # TODO: ajouter les 3 valeur dans leur liste respectie

    # TODO : pour nombre d'ordi
    # TODO : verifier l'environement

    temp = float(input("Entrez la température: "))
    poussiere = input("Entrez le niveau de poussière: ")
    humidite = float(input("Entrez l'humidité: "))
    print(environnement_optimal(temp, poussiere, humidite))
