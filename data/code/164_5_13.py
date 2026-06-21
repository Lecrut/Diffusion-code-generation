def categorize_animals():
    animal_diet = {
        'lion': 'carnivore',
        'rabbit': 'herbivore',
        'panda': 'omnivore',
        'frog': 'herbivore',
        'tiger': 'carnivore',
        'bear': 'omnivore'
    }
    
    herbivores = []
    carnivores = []
    omnivores = []
    
    for animal, diet in animal_diet.items():
        if diet == 'herbivore':
            herbivores.append(animal)
        elif diet == 'carnivore':
            carnivores.append(animal)
        elif diet == 'omnivore':
            omnivores.append(animal)
    
    return herbivores, carnivores, omnivores

if __name__ == '__main__':
    herbivores, carnivores, omnivores = categorize_animals()
    print("Herbivores:", herbivores)
    print("Carnivores:", carnivores)
    print("Omnivores:", omnivores)