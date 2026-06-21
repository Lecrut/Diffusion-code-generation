def group_animals_by_reproductive_method(animals):
    reproductive_groups = {
        'viviparous': [],
        'oviparous': []
    }
    for animal, method in animals.items():
        if method in reproductive_groups:
            reproductive_groups[method].append(animal)
        else:
            print(f"Unknown reproductive method: {method} for {animal}")
    return reproductive_groups

if __name__ == '__main__':
    sample_animals = {
        'Dog': 'viviparous',
        'Cat': 'viviparous',
        'Eagle': 'oviparous',
        'Crocodile': 'oviparous',
        'Fish': 'oviparous'
    }
    grouped_animals = group_animals_by_reproductive_method(sample_animals)
    print("--- Animals Grouped by Reproductive Method ---")
    for method, animals in grouped_animals.items():
        print(f"{method.capitalize()} Animals: {', '.join(animals)}")
    print("--------------------------------------------")