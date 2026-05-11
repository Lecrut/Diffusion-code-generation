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
        class_name: [animal for animal, class_name in animal_classes.items() if class_name == class_name]
        for class_name in set(animal_classes.values())
    }
    return grouped_animals
if __name__ == '__main__':
    result = group_animals_by_class()
    print(result)