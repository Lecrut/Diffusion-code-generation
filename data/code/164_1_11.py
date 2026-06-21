ANIMAL_TYPES = {
    "Mammal": ["Dog", "Cat"],
    "Bird": ["Bird"],
    "Fish": ["Fish"]
}

def categorize_animals(animals):
    categorized_dict = {}
    for animal_type, animals_list in ANIMAL_TYPES.items():
        categorized_dict[animal_type] = [animal for animal in animals if animal in animals_list]
    return categorized_dict

if __name__ == '__main__':
    sample_input = ["Dog", "Cat", "Bird", "Fish"]
    result = categorize_animals(sample_input)
    print(result)