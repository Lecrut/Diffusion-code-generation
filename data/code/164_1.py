def categorize_animals(raw_string):
    animal_dict = {}
    animals = raw_string.split(',')
    for animal in animals:
        animal = animal.strip()
        if animal:
            animal_dict[animal] = ["Mammal", "Vertebrate"]
    return animal_dict
if __name__ == '__main__':
    sample_input = "Dog,Cat,Bird,Fish"
    result = categorize_animals(sample_input)
    print(result)