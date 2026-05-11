def organize_animals(animal_data, hierarchy):
    organized = {}
    for animal, parent in animal_data.items():
        current_level = ""
        path = []
        temp = animal
        while temp:
            path.append(temp)
            if temp in hierarchy:
                current_level = temp
                break
            temp = hierarchy.get(temp)
        if path:
            organized[current_level] = organized.get(current_level, []) + [animal]
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
        "Mammal": "Animal",
        "Animal": "None",
        "Reptile": "None"
    }
    result = organize_animals(animal_data, hierarchy)
    print(result)