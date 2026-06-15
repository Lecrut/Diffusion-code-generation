def create_animal_dictionary():
    animal_list = ["lion", "tiger", "elephant", "monkey", "zebra"]
    animal_dict = {}
    for animal in animal_list:
        animal_dict[animal] = True
    return animal_dict
if __name__ == '__main__':
    result = create_animal_dictionary()
    print(result)