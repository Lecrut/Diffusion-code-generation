def categorize_animals():
    diets = {
        'lion': 'carnivore',
        'rabbit': 'herbivore',
        'panda': 'omnivore',
        'frog': 'herbivore',
        'tiger': 'carnivore'
    }
    
    return diets

if __name__ == '__main__':
    animal_diets = categorize_animals()
    print(animal_diets)