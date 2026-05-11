def group_animals_by_class():
    animal_list = [
        "Dog", "Cat", "Lion", "Snake", "Eagle", "Fish", "Frog", "Turtle", "Parrot", "Whale"
    ]
    classifications = {
        "Mammal": [],
        "Reptile": [],
        "Bird": [],
        "Fish": [],
        "Amphibian": [],
        "Other": []
    }
    for animal in animal_list:
        if animal == "Dog":
            classifications["Mammal"].append(animal)
        elif animal == "Cat":
            classifications["Mammal"].append(animal)
        elif animal == "Lion":
            classifications["Mammal"].append(animal)
        elif animal == "Snake":
            classifications["Reptile"].append(animal)
        elif animal == "Eagle":
            classifications["Bird"].append(animal)
        elif animal == "Fish":
            classifications["Fish"].append(animal)
        elif animal == "Frog":
            classifications["Amphibian"].append(animal)
        elif animal == "Turtle":
            classifications["Reptile"].append(animal)
        elif animal == "Parrot":
            classifications["Bird"].append(animal)
        elif animal == "Whale":
            classifications["Mammal"].append(animal)
    return classifications
if __name__ == '__main__':
    result = group_animals_by_class()
    print(result)