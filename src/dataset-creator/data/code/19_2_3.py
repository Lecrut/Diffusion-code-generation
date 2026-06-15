def create_animal_dictionary():
    animal_list = ["lion", "tiger", "elephant", "monkey", "zebra"]
    animal_dict = {}
    for animal in animal_list:
        animal_dict[animal] = True
    return animal_dict
if __name__ == '__main__':
    animal_data = create_animal_dictionary()
    print(animal_data)
    print(f"Lion is in the dictionary: {'lion' in animal_data}")
    print(f"Elephant is in the dictionary: {'elephant' in animal_data}")