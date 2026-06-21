def group_animals_by_reproductive_method(animals):
    grouped = {'viviparous': [], 'oviparous': []}
    for animal, method in animals.items():
        if method == 'viviparous':
            grouped['viviparous'].append(animal)
        elif method == 'oviparous':
            grouped['oviparous'].append(animal)
    return grouped

if __name__ == '__main__':
    sample_animals = {
        'dog': 'viviparous',
        'cat': 'viviparous',
        'bird': 'oviparous',
        'snake': 'oviparous'
    }
    print(group_animals_by_reproductive_method(sample_animals))