def organize_animals():
    animal_list = ["dog", "cat", "lion", "elephant", "tiger"]
    animal_dictionary = {}
    for animal in animal_list:
        animal_dictionary[animal] = "mammal"
    return animal_dictionary
if __name__ == '__main__':
    organized_data = organize_animals()
    print(organized_data)