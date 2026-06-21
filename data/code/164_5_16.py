def categorize_animals():
    diets = {
        'lion': 'carnivore',
        'rabbit': 'herbivore',
        'bear': 'omnivore',
        'frog': 'herbivore',
        'eagle': 'carnivore'
    }
    
    herbivores = [animal for animal, diet in diets.items() if diet == 'herbivore']
    carnivores = [animal for animal, diet in diets.items() if diet == 'carnivore']
    omnivores = [animal for animal, diet in diets.items() if diet == 'omnivore']
    
    return herbivores, carnivores, omnivores

if __name__ == '__main__':
    herbivores, carnivores, omnivores = categorize_animals()
    print("Herbivores:", herbivores)
    print("Carnivores:", carnivores)
    print("Omnivores:", omnivores)