from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/yo', methods=['GET'])
def Hello():
    return 'Yo, ici Hassane !!'

@app.route('/query', methods=['GET','POST'])
def handle_query():
    # Récupérer les données envoyées par le robot
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"message": "Requête invalide."}), 400

    user_query = data['query']

    # Exemple de traitement basique de la requête
    if "bonjour" in user_query.lower():
        response_message = "Bonjour, il fait froid aujourd'hui, tu ne trouves pas ?"
    elif "au revoir" in user_query.lower():
        response_message = "Au revoir, passez une bonne journée !"
    elif "yo" in user_query.lower():
        response_message = "Un appel est fait !"
    else:
        response_message = f"Je ne suis pas sûr de comprendre : {user_query}"

    # Retourner la réponse au robot
    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
