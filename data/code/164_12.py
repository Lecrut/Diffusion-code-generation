def organize_animals(animal_names, animal_types):
    organized = {}
    for animal in animal_names:
        if animal in animal_types:
            animal_type = animal_types[animal]
            if animal_type not in organized:
                organized[animal_type] = []
            organized[animal_type].append(animal)
    return organized
if __name__ == '__main__':
    animal_names_list = ["dog", "cat", "bird", "fish", "lion", "elephant", "snake"]
    animal_types_map = {
        "dog": "mammal",
        "cat": "mammal",
        "bird": "bird",
        "fish": "fish",
        "lion": "mammal",
        "elephant": "mammal",
        "snake": "reptile"
    }
    result = organize_animals(animal_names_list, animal_types_map)
    print(result)