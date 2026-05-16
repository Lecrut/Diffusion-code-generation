def group_animals_by_class():
    animals = [
        "Lion",
        "Dog",
        "Snake",
        "Eagle",
        "Whale",
        "Crocodile",
        "Parrot",
        "Bat",
        "Frog",
        "Shark"
    ]
    animal_classes = {
        "Lion": "Mammal",
        "Dog": "Mammal",
        "Snake": "Reptile",
        "Eagle": "Bird",
        "Whale": "Mammal",
        "Crocodile": "Reptile",
        "Parrot": "Bird",
        "Bat": "Mammal",
        "Frog": "Amphibian",
        "Shark": "Fish"
    }
    grouped_animals = {
        "Mammal": [],
        "Reptile": [],
        "Bird": [],
        "Amphibian": [],
        "Fish": []
    }
    for animal in animals:
        if animal in animal_classes:
            class_name = animal_classes[animal]
            if class_name in grouped_animals:
                grouped_animals[class_name].append(animal)
    return grouped_animals
if __name__ == '__main__':
    result = group_animals_by_class()
    print(result)