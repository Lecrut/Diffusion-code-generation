def group_animals_by_reproductive_method(animals):
    groups = {'viviparous': [], 'oviparous': []}
    for animal, method in animals.items():
        if method == 'viviparous':
            groups['viviparous'].append(animal)
        elif method == 'oviparous':
            groups['oviparous'].append(animal)
    return groups

if __name__ == '__main__':
    sample_animals = {
        'dog': 'viviparous',
        'cat': 'viviparous',
        'chicken': 'oviparous',
        'frog': 'oviparous'
    }
    print(group_animals_by_reproductive_method(sample_animals))