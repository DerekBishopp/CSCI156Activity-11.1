__author__ = 'Derek'
food = {'Sandwich': 'Easy to make meal, for people that are hungry but lazy.',
        'Pizza': 'Made to order, for those that are incompetent in the kitchen.',
        'Lasagna': 'Takes super long make, but oh so satisfying.',
        'Steak': 'Steak and potatoes, a mans meal... enough said.',
        'Tacos': 'Deliciously regretful'}
print(food)
print('\n')

print(food['Steak'])
print('\n')

print(food.get('Tacos'))
print('\n')

for goodness in food:
    print(food[goodness])
print('\n')

for goodness in food:
    if goodness == 'Pie':
        print('I like pie.')
    else:
        print('No pie here... unfortunately')