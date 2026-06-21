def group_animals_by_reproductive_method(animals):
    grouped_animals = {'viviparous': [], 'oviparous': []}
    for animal, method in animals.items():
        if method == 'viviparous':
            grouped_animals['viviparous'].append(animal)
        elif method == 'oviparous':
            grouped_animals['oviparous'].append(animal)
    return grouped_animals

if __name__ == '__main__':
    sample_animals = {
        'Dog': 'viviparous',
        'Cat': 'viviparous',
        'Chicken': 'oviparous',
        'Snake': 'oviparous',
        'Elephant': 'viviparous'
    }
    grouped_result = group_animals_by_reproductive_method(sample_animals)
    print("Viviparous Animals:", grouped_result['viviparous'])
    print("Oviparous Animals:", grouped_result['oviparous'])