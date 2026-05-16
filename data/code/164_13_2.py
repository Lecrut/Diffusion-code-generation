def process_animal_data(animal_list):
    unique_animals = set()
    animal_types = {}
    for item in animal_list:
        if not isinstance(item, str):
            print(f"Error: Invalid input type encountered: {type(item)}")
            continue
        animal_type = item.lower().strip()
        if animal_type in unique_animals:
            continue
        unique_animals.add(animal_type)
        animal_types[animal_type] = item
    return unique_animals, animal_types
if __name__ == '__main__':
    sample_animals = [
        "Dog",
        "cat",
        "Bird",
        123,
        "fish",
        "Dog",
        "Elephant",
        3.14
    ]
    unique_types, animal_map = process_animal_data(sample_animals)
    print("Unique Animal Types Found:")
    print(list(unique_types))
    print("\nAnimal to Type Mapping:")
    for animal, animal_type in animal_map.items():
        print(f"{animal}: {animal_type}")