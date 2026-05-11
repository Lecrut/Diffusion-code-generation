def organize_animals(input_string):
    animal_data = {
        "dog": "Canine",
        "cat": "Feline",
        "bird": "Avian",
        "fish": "Pisces",
        "lion": "Feline",
        "cow": "Bovine"
    }
    result = {}
    animals = [animal.strip() for animal in input_string.split(',')]
    for animal in animals:
        if animal in animal_data:
            result[animal] = animal_data[animal]
        else:
            result[animal] = "Unknown"
    return result
if __name__ == '__main__':
    sample_input = "dog,cat,bird,fish,lion,cow,snake"
    organized_dictionary = organize_animals(sample_input)
    print(organized_dictionary)