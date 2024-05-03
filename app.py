from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def load_data():
    with open('recipes/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_data(data):
    with open('recipes/data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    data = load_data()
    recipes = data['recipes']
    return render_template('index.html', recipes=recipes)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients'].split(',')
        instructions = request.form['instructions']
        new_recipe = {'title': title, 'ingredients': ingredients, 'instructions': instructions}

        data = load_data()
        data['recipes'].append(new_recipe)
        save_data(data)

        return redirect(url_for('index'))
    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)


