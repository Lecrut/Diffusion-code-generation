def sort_animals_by_type(animal_list):
    animal_types = {}
    for animal in animal_list:
        if not isinstance(animal, str):
            continue
        animal_type = animal.lower()
        if animal_type not in animal_types:
            animal_types[animal_type] = []
        animal_types[animal_type].append(animal)
    
    sorted_animals = {key: sorted(value) for key, value in animal_types.items()}
    return sorted_animals

if __name__ == '__main__':
    sample_animals = [
        "Dog",
        "cat",
        "Bird",
        "Lion",
        "fish",
        "dog"
    ]
    
    sorted_animals = sort_animals_by_type(sample_animals)
    for animal_type, animals in sorted_animals.items():
        print(f"{animal_type.capitalize()}: {', '.join(animals)}")