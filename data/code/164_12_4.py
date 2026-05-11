def organize_animals(animal_names, animal_types):
    organized_data = {}
    for animal in animal_names:
        if animal in animal_types:
            animal_type = animal_types[animal]
            if animal_type not in organized_data:
                organized_data[animal_type] = []
            organized_data[animal_type].append(animal)
    return organized_data
if __name__ == '__main__':
    sample_animal_names = ["dog", "cat", "bird", "fish", "lion", "elephant"]
    sample_animal_types = {
        "dog": "mammal",
        "cat": "mammal",
        "bird": "avian",
        "fish": "aquatic",
        "lion": "mammal",
        "elephant": "mammal"
    }
    result = organize_animals(sample_animal_names, sample_animal_types)
    print(result)