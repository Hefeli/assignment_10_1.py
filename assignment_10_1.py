
# Hirabai Renaud (1874635)
# cse20 Fall 2021
#  Python 3.9.7, 11/29/2021

# Class "Cake"
class Cake:
    # Using magic method '__init__' to set up my objects instances
    def __init__(self, ingredients, recipe, additional, extra_step):
        self._ingredients = ingredients
        self._recipe = recipe
        self._additional = additional
        self._extra_step = extra_step
        # Keep in mind, each variables has a '._' to protect their identity.
        # usig the special character "\n" to organize the layout of the code.
        print("\n")
    # Runs through the constructor and retrieves the 'recipe' method.
    def get_recipe(self):
        print(self._recipe) # prints recipe

        print("\n")
     # Runs through the constructor and retrieves the 'Ingredient' method.
    def get_ingredients(self):
        print(self._ingredients) # prints Ingredients

    print("\n")
     # Read "additional" variable and appends its info into "Basic Ingrediants".
    def add_ingredient(self):
        print(self._additional) # prints 'Additional' 
    
    print("\n")
     # Runs through the 'extra_step' variable and concatenates a list into the "Recipe" list.
    def add_extra_step(self):
        print(self._extra_step) # prints extra_step
# Main function
def main():
    # Lists and basic data for the values used in the code.
    # Ingredients: Provide he ingredients for the cake
    ingredients = [f"Ingredients--> {4}: Pheonix eggs", f"{3}lb: Hibiscus Cream Flour", f"{5}gallons: Lava Mashmallows", f"{3}gallons: Whole spun Cow milk",f"{5} metric ton: Sesame Butter" , f"{1} Skyrim: Cheese"]
    print("\n")
    # Recipe: Provides the recipe for the cake in the order 1-3 (plus one optional step)
    recipe = ["Recipe--> 1)mix a quarter of the eggs, half the milk, and all the butter in flour", "2) idk, put in 7/3 of whatever works...", "3) roast until golden using mashmallows as oven and cheese as furnace fuel"]
    # Simple append funtion that adds another Ingredient to our list.
    additional = ingredients.append("A lot of Eggplant Cream Paste")
    # A step containing a list, and an extra_step that adds that list to the recipe as a side bonus.
    step = ["4) then you could even add frosted parmesian stardust for extra flavour chills^^"]
    extra_step = recipe + step

# Assigning the Class to a variable
    cake = Cake(ingredients, recipe, additional, extra_step)
    # Calling out each methods implemented by the code.
    cake.get_ingredients()
    print("\n")
    cake.get_recipe()
    cake.add_extra_step()
    print("\n")
    # Each segment here takes the arguments from the constructor and runs through them.
    # After doing so, they will be called out to their position up top, and via the 
    # arguments provided in this main funtion, they will print out the information.
    # Something to keep in mind, is that even though the orint funtion is higher up,
    # it is here that the output may be altered, as I've down with the "\n" special characters. 
if __name__ == "__main__":
    main()


# Citations:

# https://www.geeksforgeeks.org/encapsulation-in-python/ 
# https://www.geeksforgeeks.org/g-fact-34-class-or-static-variables-in-python/ 
# https://www.youtube.com/watch?v=rq8cL2XMM5M&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&index=2
# https://www.youtube.com/watch?v=rq8cL2XMM5M 
# https://www.tutorialsteacher.com/python/magic-methods-in-python
# https://www.geeksforgeeks.org/hashing-set-1-introduction/ 
# https://medium.com/fintechexplained/advanced-python-what-are-magic-methods-d21891cf9a08 (kinda embarrased on that one)
# https://stackoverflow.com/questions/52528985/python-passing-a-list-as-argument-to-class 