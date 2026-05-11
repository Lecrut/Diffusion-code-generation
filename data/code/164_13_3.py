def process_animal_data(animal_list):
    animal_types = set()
    animal_types_map = {}
    for animal in animal_list:
        if not isinstance(animal, str):
            print(f"Error: Invalid input type for animal: {animal}")
            continue
        animal_types.add(animal.lower())
        animal_types_map[animal] = animal.lower()
    return animal_types, animal_types_map
if __name__ == '__main__':
    sample_animals = [
        "Dog",
        "Cat",
        "bird",
        123,
        "Fish",
        "Dog",
        "snake"
    ]
    unique_types, mapping = process_animal_data(sample_animals)
    print("Unique Animal Types:")
    print(unique_types)
    print("\nAnimal to Type Mapping:")
    for animal, animal_type in mapping.items():
        print(f"{animal}: {animal_type}")