def group_animals_by_legs(animals):
    grouped = {}
    for animal, legs in animals.items():
        if legs not in grouped:
            grouped[legs] = []
        grouped[legs].append(animal)
    return grouped

if __name__ == '__main__':
    sample_animals = {
        "lion": 4,
        "tiger": 4,
        "frog": 4,
        "octopus": 8,
        "snake": 0
    }
    result = group_animals_by_legs(sample_animals)
    print(result)