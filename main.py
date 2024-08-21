import customtkinter as ctk
from tkinter import messagebox

# Définir un style plus clair et moderne
ctk.set_appearance_mode("light")  # Mode clair
ctk.set_default_color_theme("green")  # Thème "green"

def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4.33

def salaire_journalier(salaire_hebdomadaire, jours_travailles):
    return salaire_hebdomadaire / jours_travailles

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

def afficher_resultat_sequentiel(resultat, label, couleur, delai):
    root.after(delai, lambda: label.configure(text=resultat, fg_color=couleur))

def calculer_salaires():
    try:
        salaire_annuel = float(entry_salaire_annuel.get())
        heures_travaillees = float(entry_heures_travaillees.get())
        jours_travailles = float(entry_jours_travailles.get())

        if salaire_annuel <= 0 or heures_travaillees <= 0 or jours_travailles <= 0:
            raise ValueError("Tous les champs doivent être positifs.")

        mensuel = salaire_mensuel(salaire_annuel)
        hebdomadaire = salaire_hebdomadaire(mensuel)
        journalier = salaire_journalier(hebdomadaire, jours_travailles)
        horaire = salaire_horaire(hebdomadaire, heures_travaillees)

        # Affichage séquentiel des résultats
        afficher_resultat_sequentiel(f"Salaire mensuel : {mensuel:.2f} euros", label_resultat_mensuel, "lightgreen", 500)
        afficher_resultat_sequentiel(f"Salaire hebdomadaire : {hebdomadaire:.2f} euros", label_resultat_hebdomadaire, "lightblue", 1500)
        afficher_resultat_sequentiel(f"Salaire journalier : {journalier:.2f} euros", label_resultat_journalier, "lightyellow", 2500)
        afficher_resultat_sequentiel(f"Salaire horaire : {horaire:.2f} euros", label_resultat_horaire, "lightcoral", 3500)

    except ValueError as e:
        messagebox.showerror("Erreur", f"Erreur de saisie : {e}")

# Création de la fenêtre principale
root = ctk.CTk()
root.title("Calculateur de Salaires")
root.geometry("400x500")

# Widgets modernisés
entry_salaire_annuel = ctk.CTkEntry(root, placeholder_text="Salaire annuel", width=300, height=35, border_width=2, corner_radius=10)
entry_salaire_annuel.pack(pady=10)

entry_heures_travaillees = ctk.CTkEntry(root, placeholder_text="Heures travaillées par semaine", width=300, height=35, border_width=2, corner_radius=10)
entry_heures_travaillees.pack(pady=10)

entry_jours_travailles = ctk.CTkEntry(root, placeholder_text="Jours travaillés par semaine", width=300, height=35, border_width=2, corner_radius=10)
entry_jours_travailles.pack(pady=10)

# Bouton modernisé
bouton_calculer = ctk.CTkButton(root, text="Calculer", command=calculer_salaires, width=150, height=40, corner_radius=10)
bouton_calculer.pack(pady=20)

# Labels modernisés pour afficher les résultats (sans couleur initialement)
label_resultat_mensuel = ctk.CTkLabel(root, text="", width=300, height=35, corner_radius=10, text_color="black", font=("Helvetica", 14, "bold"))
label_resultat_mensuel.pack(pady=5)

label_resultat_hebdomadaire = ctk.CTkLabel(root, text="", width=300, height=35, corner_radius=10, text_color="black", font=("Helvetica", 14, "bold"))
label_resultat_hebdomadaire.pack(pady=5)

label_resultat_journalier = ctk.CTkLabel(root, text="", width=300, height=35, corner_radius=10, text_color="black", font=("Helvetica", 14, "bold"))
label_resultat_journalier.pack(pady=5)

label_resultat_horaire = ctk.CTkLabel(root, text="", width=300, height=35, corner_radius=10, text_color="black", font=("Helvetica", 14, "bold"))
label_resultat_horaire.pack(pady=5)

# Boucle principale de l'application
root.mainloop()
