def categorize_animals(animal_diet):
    categories = {
        'herbivore': ['rabbit', 'deer', 'sheep'],
        'carnivore': ['lion', 'tiger', 'wolf'],
        'omnivore': ['bear', 'panda', 'crow']
    }
    
    return {animal: category for animal, diet in animal_diet.items() if diet in categories}

if __name__ == '__main__':
    sample_animals = {
        'rabbit': 'herbivore',
        'lion': 'carnivore',
        'panda': 'omnivore',
        'frog': 'unknown'
    }
    
    categorized_animals = categorize_animals(sample_animals)
    print(categorized_animals)