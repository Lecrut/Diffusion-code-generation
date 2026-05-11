def organize_animals():
    animal_list = ["dog", "cat", "bird", "fish", "lion", "elephant"]
    animal_dictionary = {}
    for animal in animal_list:
        animal_dictionary[animal] = "mammal" if animal in ["dog", "cat", "lion", "elephant"] else ("bird" if animal == "bird" else "fish")
    return animal_dictionary
if __name__ == '__main__':
    organized_data = organize_animals()
    print(organized_data)