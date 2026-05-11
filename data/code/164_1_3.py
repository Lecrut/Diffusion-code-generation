def process_animal_string(raw_string):
    animal_dict = {}
    animals = raw_string.split(',')
    for animal in animals:
        animal = animal.strip()
        if animal:
            animal_dict[animal] = ["Category A", "Category B", "Category C"]
    return animal_dict
if __name__ == '__main__':
    sample_input = "dog,cat,bird,fish"
    result = process_animal_string(sample_input)
    print(result)