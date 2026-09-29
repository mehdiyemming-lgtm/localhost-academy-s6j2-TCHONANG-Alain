# name=" TCHONANG "
# surname=" Alain"
# age = "29"
# ville=" yaounde"
# taille =" 1.83"
# etudiant= True




# print(f"je me nomme  {name}, {surname}")
# print(f" j'ai {age} ans et je fais {taille} comme taille et je resides dans la ville de {ville}")
# age =int(age)
# taille = float(taille)

# print(type(name), type(surname))
# print (type (etudiant))
# print(type(age), type(taille ))



# # question 2
# # Bon bon le fait qu il change trois fois de suite est du a la facon dont on le declare cest le dynamisme 
# # on appelle ca le typage dynamique
# # =18 c est un int
# # ="18" c est un string
# # =18.0 c est un float 

# a= 17
# b= 5


# sum= a+ b
# prod= a* b 
# sub = a - b 
# div = a/ b 

# print(f"la somme de a et b est {sum}")
# print(f"le produit  de a et b est {prod}")
# print(f"la soustraction de a et b est {sub}")
# print(f"la division de a et b est {div}")


# quot = a//b 
# reste = a % b 
# puis = a**b 

# print(f" le quotient entier de a et b est {quot}")
# print(f"le rest de la division euclidienne  de a et b est {reste}")
# print(f"la valeur de a puissance b est {puis}")


# print( f"Est ce que a>b ? {a>b}" )
# print (f"Est ce que a<b {a<b}")
# print (f"Est ce que a==b {a==b}")
# print (f"est ce que a est different de b {a!=b}")

# print(f"a>10: {a>10}")
# print(f"a<10: {a<10}")
# print(f"b>10: {b>10}")
# print(f"b<10: {b<10}")

# num1 = float(input("Entrez un nombre pour continuer: "))
# num2 = float(input("Entrez un autre nombre pour continuer: "))

# sum = num1 + num2
# print(f"La somme de {num1} et {num2} est: {sum}")       
# prod= num1 * num2
# print(f"Le produit de {num1} et {num2} est: {prod}")       
# sub = num1 - num2
# print(f"La soustraction de {num1} et {num2} est: {sub}")       


# prenom = "Alice"
# age = float(input("Quel age avez-vous ? "))
# print("Bonjour " + prenom + ", vous avez " + str(age) + " ans.") 
# print("Dans 5 ans vous aurez " + str(age + 5) + " ans.") 
# print("Votre prenom en majuscules : " + prenom.upper())

# TypeError: print can only concatenate str (not "float") to str
# NameError: name 'Prenom' is not defined.



# produit= input ("Donnez le nom du produit")
# prix_unitaire = float (input(" Donnez le prix du produit "))
# qtite= int(input("Donnez la quantite de produit que vous voulez"))
# total=prix_unitaire* qtite


# print(" Produit: " + produit)
# print(" Prix unitaire: " + str(prix_unitaire))
# print(" Quantite: " + str(qtite))
# print(f"Le total pour {qtite} {produit}(s) est: {total}")



# fruits = ["pomme", "banane", "orange", "kiwi", "mangue"]
# fruit = 2
# for fruit in fruits:
#     print(fruit)


Nourriture = [ {"nom": "riz", "bon": False,},
              {"nom": "haricot", "bon": True,}
            ]


def ajouter_nourriture(nourriture):
    Nourriture.append(nourriture)

def terminee(nourriture):
    nourriture["bon"] = True

def afficher_nourriture():
    for nourriture in Nourriture:
        print(f"if [nourriture['bon'] == True] {nourriture['nom']} c est termine")
        


