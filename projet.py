# Librairie(s) utilisée(s)
from flask import *
import sqlite3



def renvoie():
    '''
    Cette fonction renvoie les élements de la table sous forme de tuples
    '''
    # Ouverture de la connection à la base de donnée
    connexion = sqlite3.connect('sneakers.db')
    cursor = connexion.cursor()

    resultat = cursor.execute("""SELECT * FROM sneakers""")
    elements = resultat.fetchall()
    
    # Fermeture de la connection avec la base
    connexion.close()
    
    # Retourne la liste des éléménts
    return elements


def utiliser_table(table):
    '''
    Cette fonction va nous permettre d'enregistrer les commandes SQL
    '''
    
    # Ouverture de la connection à la base de donnée
    connexion = sqlite3.connect('sneakers.db')
    cursor = connexion.cursor()
    
    # Si elle se retrouve fausse, nous passons à une deuxième technique
    cursor.execute(""" INSERT INTO sneakers VALUES (?, ?, ?, ?, ?)""",
                   table);  
    
    connexion.commit()
    
    # Fermeture de la connexion avec la base
    connexion.close()


# Création d'un objet application web Flask
app = Flask(__name__)

elements = renvoie()

# Pour génerer la première page web dynamique
@app.route("/index")

# Création d'une fonction p1 associée à l'URL "/p1"
def page1():
    """ Affiche la page index """
    # On retourne le template
    return render_template("index.html")

# Pour generer la deuxieme page web dynamique
@app.route("/homme")

# Création de la fonction p2 associé à l'URL "/p2"
def page2():
    """ Affiche la page homme """
    # On retourne le template
    return render_template("homme.html")

# Pour generer la troisième page web dynamique
@app.route("/femme")

# Création de la fonction p3 associé à l'URL "/p3"
def page3():
    """ Affiche la page femme """
    elements = renvoie()
    # On retourne le template
    return render_template("femme.html", elements = elements)

@app.route("/accessoires")

# Création de la fonction p4 associé à l'URL "/p4"
def page4():
    """ Affiche la page accessoires """
    # On retourne le template
    return render_template("accessoires.html")
    
@app.route("/requete", methods = ["POST"])
def requete2():
    ''' recupère les informations du client et les affecte des variable '''
    
    Modèle = request.form["Modèle"]
    Marque = request.form["Marque"]
    Prix = request.form["Prix"]
    
    liste = [Modèle, Marque, Prix]
    
    
    
    utiliser_table(liste)
    return page3()
    
    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port= 8000, debug=True)
