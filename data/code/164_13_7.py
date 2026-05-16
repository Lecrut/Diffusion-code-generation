def process_animal_data(animal_list):
    unique_animals = set()
    animal_types = {}
    for animal in animal_list:
        if not isinstance(animal, str):
            print(f"Error: Invalid input type for animal: {animal}")
            continue
        unique_animals.add(animal.lower())
        if animal in animal_types:
            continue
        animal_types[animal.lower()] = animal
    return unique_animals, animal_types
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
    unique_types, animal_map = process_animal_data(sample_animals)
    print("Unique Animal Types (Set):")
    print(unique_types)
    print("\nAnimal to Type Mapping (Dictionary):")
    for animal, animal_type in animal_map.items():
        print(f"{animal}: {animal_type}")