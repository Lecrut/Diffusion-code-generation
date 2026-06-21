def group_animals_by_reproductive_method(animals):
    viviparous = []
    oviparous = []

    for animal in animals:
        if 'reproductive_method' in animal and animal['reproductive_method'] == 'viviparous':
            viviparous.append(animal)
        elif 'reproductive_method' in animal and animal['reproductive_method'] == 'oviparous':
            oviparous.append(animal)

    return {'viviparous': viviparous, 'oviparous': oviparous}

if __name__ == '__main__':
    animals = [
        {'name': 'Dog', 'reproductive_method': 'viviparous'},
        {'name': 'Cat', 'reproductive_method': 'viviparous'},
        {'name': 'Chicken', 'reproductive_method': 'oviparous'},
        {'name': 'Fish', 'reproductive_method': 'oviparous'}
    ]

    grouped_animals = group_animals_by_reproductive_method(animals)
    print(grouped_animals)