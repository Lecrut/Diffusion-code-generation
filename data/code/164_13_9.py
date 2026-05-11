def process_animal_data(animal_list):
    unique_animals = set()
    animal_types = {}
    for animal in animal_list:
        if not isinstance(animal, str):
            raise TypeError("Invalid input: Animal must be a string.")
        unique_animals.add(animal.lower())
        animal_types[animal.lower()] = animal
    return unique_animals, animal_types
if __name__ == '__main__':
    sample_animals = [
        "Dog",
        "cat",
        "Bird",
        "dog",
        123,
        "Fish"
    ]
    try:
        unique_types, animal_map = process_animal_data(sample_animals)
        print("Unique Animal Types (Set):")
        print(unique_types)
        print("\nAnimal to Type Mapping (Dictionary):")
        for animal, animal_type in animal_map.items():
            print(f"{animal}: {animal_type}")
    except TypeError as e:
        print(f"Error processing data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")