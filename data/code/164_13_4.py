def process_animal_data(animal_list):
    unique_animals = set()
    animal_types = {}
    for item in animal_list:
        if not isinstance(item, str):
            print(f"Error: Invalid input type encountered: {type(item)}")
            continue
        animal_type = item.lower().strip()
        if animal_type in unique_animals:
            print(f"Warning: Duplicate animal type '{animal_type}' found and skipped.")
            continue
        unique_animals.add(animal_type)
        animal_types[animal_type] = item
    return unique_animals, animal_types
if __name__ == '__main__':
    sample_animals = [
        "Dog",
        "cat",
        "Bird",
        "dog",
        123,
        "Fish",
        "cat",
        "Elephant"
    ]
    unique_types, mapping = process_animal_data(sample_animals)
    print("--- Unique Animal Types ---")
    print(unique_types)
    print("\n--- Animal to Type Mapping ---")
    for animal, animal_type in mapping.items():
        print(f"{animal}: {animal_type}")