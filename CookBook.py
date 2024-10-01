import json  # Used for handling JSON data
import requests  # Library for making HTTP requests
from pywebio.output import put_html, clear, put_buttons  # For managing output to the UI
from pywebio.session import hold  # For session control

API_KEY = "945125345d564068a7b30197ca87dae2"  # Food API key

def get_random_recipe():
    clear()  # Clear the current screen
    
    put_html('<h2 style="color: #00695c;">🍽️ Random Recipe 🍽️</h2>')  # Header for the recipe section
    
    # API URL for fetching random recipes
    url = "https://api.spoonacular.com/recipes/random"
    
   # creates dictionairy called params, used to store parameters
    params = {
        'apiKey': API_KEY  # API key
    }
    
    try:
        # Make a GET request to fetch a random recipe
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            recipe = data['recipes'][0]  # Get the first recipe from the list
            
            # Extract recipe details
            recipe_title = recipe['title']  # Recipe title
            recipe_summary = recipe['summary']  # Recipe summary
            recipe_image = recipe['image']  # URL of the recipe image
            
            # Display the recipe information
            put_html(f"<h3>{recipe_title}</h3>")  # Display recipe title
            put_html(f"<p>{recipe_summary}</p>")  # Display recipe summary
            put_html(f"<img src='{recipe_image}' alt='{recipe_title}' style='width:300px;' />")  # Display recipe image
            
        else:
            # Display error message if the request was not successful
            put_html(f"<p>Error fetching recipe: {response.status_code} - {response.text}</p>")
    except Exception as e:
        # Display exception message if an error occurred during the request
        put_html(f"<p>Exception occurred: {str(e)}</p>")

    # Add a button to refresh and get another random recipe
    put_buttons(
        [dict(label='🔄 Get Another Recipe', value='outline-success', color='outline-success')],
        onclick=lambda _: get_random_recipe()  # Wrap the function in a lambda to ignore the argument
    )

# Driver code
if __name__ == '__main__':
    get_random_recipe()  # Call the function to fetch and display a random recipe
    hold()  # Keep the app session running

