def group_animals_by_class():
    animal_list = [
        "Lion",
        "Dog",
        "Snake",
        "Eagle",
        "Whale",
        "Crocodile",
        "Parrot",
        "Bat",
        "Frog",
        "Elephant"
    ]
    classifications = {
        "Mammal": [],
        "Reptile": [],
        "Bird": [],
        "Amphibian": []
    }
    for animal in animal_list:
        if animal == "Lion":
            classifications["Mammal"].append(animal)
        elif animal == "Dog":
            classifications["Mammal"].append(animal)
        elif animal == "Snake":
            classifications["Reptile"].append(animal)
        elif animal == "Eagle":
            classifications["Bird"].append(animal)
        elif animal == "Whale":
            classifications["Mammal"].append(animal)
        elif animal == "Crocodile":
            classifications["Reptile"].append(animal)
        elif animal == "Parrot":
            classifications["Bird"].append(animal)
        elif animal == "Bat":
            classifications["Mammal"].append(animal)
        elif animal == "Frog":
            classifications["Amphibian"].append(animal)
        elif animal == "Elephant":
            classifications["Mammal"].append(animal)
    result = {
        "Mammal": classifications["Mammal"],
        "Reptile": classifications["Reptile"],
        "Bird": classifications["Bird"],
        "Amphibian": classifications["Amphibian"]
    }
    return result
if __name__ == '__main__':
    grouped_data = group_animals_by_class()
    print(grouped_data)