#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    print(recipe)
    print(ingredients, '\n')
    print('\n')

    for i in recipe:
        batch_total = None
        # print('recipe needs', i)
        needed_recipe = i
        amount_needed = recipe[i]
        print('1.current batch_total', batch_total)
        for j in ingredients:
            print('2.current batch_total', batch_total)
            if needed_recipe == j:
                if not batch_total:
                    batch_total = ingredients[j] // amount_needed
                print(
                    f'ingredients are, {j}({ingredients[j]}), \nrecipe calls for: {needed_recipe}({amount_needed})\n batches of {needed_recipe}:{batch_total}')
                print('3.current batch_total', batch_total)
            else:
                batch_total = 0
    return batch_total


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
