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
        if animal.startswith("type:"):
            try:
                animal_name = animal.split(":", 1)[1].strip()
                if animal_name:
                    animal_types[animal] = animal_name
            except IndexError:
                print(f"Error: Malformed type entry: {animal}")
        else:
            animal_types[animal] = "Unknown"
    return unique_animals, animal_types
if __name__ == '__main__':
    sample_data = [
        "dog",
        "cat",
        "bird",
        "dog",
        "fish",
        "type:dog:mammal",
        "type:cat:mammal",
        "type:bird:avian",
        123,
        "fish"
    ]
    unique_types, animal_map = process_animal_data(sample_data)
    print("Unique Animal Types Found:")
    print(unique_types)
    print("\nAnimal to Type Mapping:")
    for animal, animal_type in animal_map.items():
        print(f"{animal}: {animal_type}")