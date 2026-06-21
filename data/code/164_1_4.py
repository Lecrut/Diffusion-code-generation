def categorize_animals(animals):
    categories = {}
    for animal in animals:
        if 'Mammal' in animal:
            category = 'Mammals'
        elif 'Bird' in animal:
            category = 'Birds'
        elif 'Fish' in animal:
            category = 'Fishes'
        else:
            category = 'Other'
        if category not in categories:
            categories[category] = []
        categories[category].append(animal)
    return categories

if __name__ == '__main__':
    animals = ['Lion', 'Eagle', 'Salmon', 'Turtle', 'Penguin']
    print(categorize_animals(animals))