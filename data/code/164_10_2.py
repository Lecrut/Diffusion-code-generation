def organize_animals():
    animal_data = {
        "Lion": ["Mammals", "Carnivora"],
        "Eagle": ["Birds", "Aves"],
        "Snake": ["Reptiles", "Serpentes"],
        "Frog": ["Amphibians", "Anura"],
        "Whale": ["Mammals", "Cetacea"]
    }
    return animal_data
if __name__ == '__main__':
    organized_data = organize_animals()
    print(organized_data)