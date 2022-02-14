import csv

# Ecrivez le code ci-dessous. Utilisez le package csv ! 

# Créer une en-têtes de sortie
en_tete = ["nom", "salaire"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « output.csv »
with open('output.csv', 'w') as fichier_csv_out:
    # Créer un objet writer (écriture) avec ce fichier TEST
    writer = csv.writer(fichier_csv_out, delimiter=',')
    # Injection entete
    writer.writerow(en_tete)

    # Lecture du csv en entrée
    with open('input.csv') as fichier_csv_in:
        reader = csv.DictReader(fichier_csv_in, delimiter=',')

        # Pour chaque ligne lue
        for ligne in reader:
            # On calcul le montant du salaire
            salaire = (int(ligne['heures_travaillees']) * 15)
            # On injecte le tout dans le fichier de sortie
            ligne = [ligne['nom'], salaire]
            writer.writerow(ligne)
