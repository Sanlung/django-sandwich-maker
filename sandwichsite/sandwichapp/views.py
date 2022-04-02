from django.shortcuts import render
from django.views import View
from django.http import Http404
import random

ingredients = {
    'meats': ['corned beef', 'pastrami', 'honey turkey', 'pepper steak', 'veggie burger'],
    'cheeses': ['american', 'swiss', 'provolone', 'cheddar', 'mozzarella'],
    'toppings': ['lettuce', 'tomato', 'onions', 'peppers', 'pickles']
}

class SandwichappView(View):
    def get(self, request):
        if request.method == 'GET':
            return render(
                request = request,
                template_name = 'sandwichapp.html',
                context = {'ingredients': ingredients.keys()}
                )

class IngredientsListView(View):
    def get(self, request, ingredient_type):
        if request.method == 'GET':
            if ingredient_type not in ingredients:
                raise Http404(f'No such ingredient: {ingredient_type.title()}')
            return render(
                request = request,
                template_name = 'ingredients_list.html',
                context = {
                    'ingredients': ingredients[ingredient_type],
                    'ingredient_type': ingredient_type,
                }
            )

class SandwichGeneratorView(View):
    def get(self, request):
        if request.method == 'GET':
            random_meat = random.choice(ingredients['meats'])
            random_cheese = random.choice(ingredients['cheeses'])
            random_topping = random.choice(ingredients['toppings'])

            sandwich = f'{random_meat} & {random_cheese} with {random_topping}'

            return render(
                request = request,
                template_name = 'sandwich_generator.html',
                context = {'sandwich': sandwich},
            )
