def process_animal_data(animal_list):
    unique_animals = set()
    animal_types = {}
    for item in animal_list:
        if not isinstance(item, str):
            print(f"Error: Invalid input type encountered: {type(item)}")
            continue
        animal_name = item.strip()
        if not animal_name:
            continue
        if animal_name in unique_animals:
            continue
        unique_animals.add(animal_name)
        animal_types[animal_name] = "Unknown"
    return unique_animals, animal_types
if __name__ == '__main__':
    sample_animals = [
        "Lion",
        "Tiger",
        "Elephant",
        "lion",
        123,
        "Bear",
        "Elephant",
        None
    ]
    unique_types, animal_map = process_animal_data(sample_animals)
    print("Unique Animals Found:")
    print(list(unique_types))
    print("\nAnimal to Type Mapping:")
    for animal, animal_type in animal_map.items():
        print(f"{animal}: {animal_type}")