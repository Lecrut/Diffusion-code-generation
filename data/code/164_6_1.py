def group_animals_by_class():
    animal_list = [
        "Lion",
        "Dog",
        "Snake",
        "Eagle",
        "Whale",
        "Lizard",
        "Parrot",
        "Bat",
        "Crocodile",
        "Elephant"
    ]
    animal_classes = {
        "Lion": "Mammal",
        "Dog": "Mammal",
        "Snake": "Reptile",
        "Eagle": "Bird",
        "Whale": "Mammal",
        "Lizard": "Reptile",
        "Parrot": "Bird",
        "Bat": "Mammal",
        "Crocodile": "Reptile",
        "Elephant": "Mammal"
    }
    grouped_animals = {
        class_name: [animal for animal, class_name in animal_classes.items() if class_name == class_name]
        for class_name in set(animal_classes.values())
    }
    return grouped_animals
if __name__ == '__main__':
    result = group_animals_by_class()
    print(result)