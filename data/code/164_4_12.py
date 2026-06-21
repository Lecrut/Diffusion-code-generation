def validate_animals(animals):
    if not isinstance(animals, dict):
        raise ValueError("Input must be a dictionary")
    for animal, legs in animals.items():
        if not isinstance(animal, str) or not isinstance(legs, int):
            raise ValueError("Invalid animal or legs value")

def group_animals_by_legs(animals):
    validate_animals(animals)
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