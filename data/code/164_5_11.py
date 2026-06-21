def categorize_animals():
    diets = {
        'lion': 'carnivore',
        'rabbit': 'herbivore',
        'panda': 'omnivore',
        'frog': 'herbivore',
        'tiger': 'carnivore',
        'bear': 'omnivore'
    }
    
    return diets

if __name__ == '__main__':
    animal_diet = categorize_animals()
    print(animal_diet)