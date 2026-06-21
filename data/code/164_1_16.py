def validate_animal_list(animal_list):
    if not isinstance(animal_list, list):
        raise ValueError("Input must be a list")
    for item in animal_list:
        if not isinstance(item, str) or not item.strip():
            raise ValueError("List items must be non-empty strings")

def categorize_animals(animal_list):
    validate_animal_list(animal_list)
    animal_dict = {}
    animal_types = ["Mammal", "Vertebrate"]
    for animal in animal_list:
        animal_type = ", ".join(animal_types)
        if animal not in animal_dict:
            animal_dict[animal] = [animal_type]
    return animal_dict

if __name__ == '__main__':
    sample_input = ["Dog", "Cat", "Bird", "Fish"]
    result = categorize_animals(sample_input)
    print(result)