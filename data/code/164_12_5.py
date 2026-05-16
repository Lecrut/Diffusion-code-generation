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
    animal_names_list = ["dog", "cat", "bird", "fish", "lion", "elephant", "snake"]
    animal_types_map = {
        "dog": "mammal",
        "cat": "mammal",
        "bird": "bird",
        "fish": "aquatic",
        "lion": "mammal",
        "elephant": "mammal",
        "snake": "reptile"
    }
    result = organize_animals(animal_names_list, animal_types_map)
    print(result)