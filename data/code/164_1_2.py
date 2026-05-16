def categorize_animals(raw_string):
    animal_dict = {}
    animals = raw_string.split(',')
    for animal in animals:
        animal_name = animal.strip()
        if animal_name:
            animal_dict[animal_name] = []
    return animal_dict
if __name__ == '__main__':
    sample_input = "dog,cat,bird,fish"
    result = categorize_animals(sample_input)
    print(result)