def group_animals_by_legs(animals):
    grouped = {}
    for animal, legs in animals.items():
        if legs not in grouped:
            grouped[legs] = []
        grouped[legs].append(animal)
    return grouped

if __name__ == '__main__':
    sample_animals = {
        "dog": 4,
        "cat": 4,
        "spider": 8,
        "ant": 6,
        "bird": 2
    }
    print(group_animals_by_legs(sample_animals))