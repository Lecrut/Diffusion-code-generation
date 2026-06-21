def group_animals_by_legs(animals):
    grouped = {}
    for animal, legs in animals.items():
        if legs not in grouped:
            grouped[legs] = []
        grouped[legs].append(animal)
    return grouped

if __name__ == '__main__':
    sample_animals = {
        "elephant": 4,
        "lion": 4,
        "snake": 0,
        "horse": 4,
        "crab": 8
    }
    result = group_animals_by_legs(sample_animals)
    print(result)