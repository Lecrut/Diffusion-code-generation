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
        if category not in categories:
            categories[category] = []
        categories[category].append(animal)
    return categories

if __name__ == '__main__':
    sample_animals = ['lion', 'eagle', 'salmon', 'frog', 'tiger', 'penguin']
    print(categorize_animals(sample_animals))