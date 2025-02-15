import requests

# Your Spoonacular API key
API_KEY = "bfd2a9a51c6246d1888d6ac2c820e72a"
BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"

def get_recipes(ingredients):
    """Fetch recipes based on ingredients using Spoonacular API."""
    # Prepare API request parameters
    params = {
        "ingredients": ",".join(ingredients),
        "number": 5,  # Number of recipes to return
        "ranking": 1,  # Rank recipes by minimizing missing ingredients
        "apiKey": API_KEY,
    }

    # Make the API call
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        recipes = response.json()
        return recipes
    else:
        print("Error:", response.json())
        return None

def display_recipes(recipes):
    """Display fetched recipes."""
    if recipes:
        print("\nHere are some recipes you can try:")
        for i, recipe in enumerate(recipes, start=1):
            print(f"{i}. {recipe['title']}")
            print(f"   - Missing Ingredients: {[ingredient['name'] for ingredient in recipe['missedIngredients']]}")
            print(f"   - Recipe Link: https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-').lower()}-{recipe['id']}")
    else:
        print("\nNo recipes found. Try using more ingredients!")

def main():
    print("Welcome to the Recipe Recommendation Bot!")
    print("Enter the ingredients you have (separated by commas):")
    user_input = input("> ").lower()
    user_ingredients = [ingredient.strip() for ingredient in user_input.split(",")]

    recipes = get_recipes(user_ingredients)
    display_recipes(recipes)

if __name__ == "__main__":
    main()
