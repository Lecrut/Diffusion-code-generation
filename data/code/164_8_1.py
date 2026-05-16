def organize_animals(input_string):
    animal_categories = {
        "dog": "Canine",
        "cat": "Feline",
        "bird": "Avian",
        "fish": "Aquatic",
        "lion": "Feline",
        "cow": "Bovine"
    }
    result_dict = {}
    animals = [animal.strip() for animal in input_string.split(',')]
    for animal in animals:
        if animal in animal_categories:
            result_dict[animal] = animal_categories[animal]
        else:
            result_dict[animal] = "Unknown"
    return result_dict
if __name__ == '__main__':
    sample_input = "dog,cat,bird,fish,lion,cow,snake"
    organized_data = organize_animals(sample_input)
    print(organized_data)