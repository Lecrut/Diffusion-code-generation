def categorize_animals(animals):
    diet_categories = {
        'herbivore': ['rabbit', 'deer', 'sheep'],
        'carnivore': ['lion', 'tiger', 'wolf'],
        'omnivore': ['bear', 'panda', 'crow']
    }
    
    categorized_animals = {'herbivore': [], 'carnivore': [], 'omnivore': []}
    
    for animal in animals:
        if animal in diet_categories['herbivore']:
            categorized_animals['herbivore'].append(animal)
        elif animal in diet_categories['carnivore']:
            categorized_animals['carnivore'].append(animal)
        elif animal in diet_categories['omnivore']:
            categorized_animals['omnivore'].append(animal)
    
    return categorized_animals

if __name__ == '__main__':
    animals = ['rabbit', 'lion', 'panda', 'deer']
    print(categorize_animals(animals))