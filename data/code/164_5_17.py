def categorize_animals(animals):
    diet_categories = {
        'herbivore': ['rabbit', 'deer', 'sheep'],
        'carnivore': ['lion', 'tiger', 'wolf'],
        'omnivore': ['bear', 'panda', 'crow']
    }
    categorized_animals = {category: [] for category in diet_categories}
    
    for animal, diet in animals.items():
        if diet in diet_categories['herbivore']:
            categorized_animals['herbivore'].append(animal)
        elif diet in diet_categories['carnivore']:
            categorized_animals['carnivore'].append(animal)
        elif diet in diet_categories['omnivore']:
            categorized_animals['omnivore'].append(animal)
    
    return categorized_animals

if __name__ == '__main__':
    animals = {
        'rabbit': 'herbivore',
        'lion': 'carnivore',
        'panda': 'omnivore'
    }
    print(categorize_animals(animals))