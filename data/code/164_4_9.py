def group_animals_by_legs(animals):
    groups = {}
    for animal, legs in animals.items():
        if legs not in groups:
            groups[legs] = []
        groups[legs].append(animal)
    return groups

if __name__ == '__main__':
    sample_animals = {
        'dog': 4,
        'cat': 4,
        'spider': 8,
        'bird': 2,
        'snake': 0
    }
    print(group_animals_by_legs(sample_animals))