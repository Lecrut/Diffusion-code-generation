def create_animal_dictionary():
    animal_list = ["lion", "tiger", "elephant", "monkey", "zebra"]
    animal_dict = {}
    for animal in animal_list:
        animal_dict[animal] = True
    return animal_dict
if __name__ == '__main__':
    animals = create_animal_dictionary()
    print(animals)
    print(f"Lion is in the dictionary: {'lion' in animals}")
    print(f"Elephant is in the dictionary: {'elephant' in animals}")