def categorize_animals(animals):
    categories = {
        'forest': [],
        'ocean': [],
        'desert': []
    }
    for animal, habitat in animals.items():
        if habitat == 'forest':
            categories['forest'].append(animal)
        elif habitat == 'ocean':
            categories['ocean'].append(animal)
        elif habitat == 'desert':
            categories['desert'].append(animal)
    return categories

if __name__ == '__main__':
    animals = {
        'lion': 'forest',
        'tiger': 'forest',
        'shark': 'ocean',
        'dolphin': 'ocean',
        'camel': 'desert',
        'rabbit': 'forest'
    }
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)