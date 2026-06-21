def categorize_animals(animals):
    categories = {}
    for animal in animals:
        if 'mammal' in animal.lower():
            category = 'Mammals'
        elif 'bird' in animal.lower():
            category = 'Birds'
        elif 'fish' in animal.lower():
            category = 'Fish'
        else:
            category = 'Other'
        categories.setdefault(category, []).append(animal)
    return categories

if __name__ == '__main__':
    animals = ['lion', 'tiger', 'eagle', 'penguin', 'salmon', 'shark']
    print(categorize_animals(animals))