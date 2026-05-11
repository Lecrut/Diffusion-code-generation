def organize_animals(animal_data, hierarchy):
    organized = {}
    for animal, parent in animal_data.items():
        current_level = parent
        path = []
        temp = animal
        while current_level is not None:
            path.append(current_level)
            if current_level in hierarchy:
                current_level = hierarchy[current_level]
            else:
                break
        if path:
            root = path[0]
            if root not in organized:
                organized[root] = []
            organized[root].append(animal)
    return organized
if __name__ == '__main__':
    animal_data = {
        "Dog": "Mammal",
        "Cat": "Mammal",
        "Whale": "Mammal",
        "Lion": "Mammal",
        "Fish": "Animal",
        "Bird": "Animal",
        "Snake": "Reptile"
    }
    hierarchy = {
        "Mammal": None,
        "Animal": None,
        "Reptile": None
    }
    result = organize_animals(animal_data, hierarchy)
    print(result)