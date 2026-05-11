def organize_animals(animal_data, hierarchy):
    organized = {}
    for animal, group in animal_data.items():
        current_level = animal
        path = []
        found = False
        for i in range(len(hierarchy)):
            if animal == hierarchy[i]:
                current_level = hierarchy[i]
                path.append(current_level)
                found = True
                break
        if found:
            organized.setdefault(current_level, []).append(animal)
    return organized
if __name__ == '__main__':
    animal_data = {
        "Dog": ["Fido", "Buddy"],
        "Cat": ["Whiskers", "Shadow"],
        "Mammal": ["Dog", "Cat"],
        "Animal": ["Dog", "Cat", "Bird"]
    }
    hierarchy = [
        "Mammal",
        "Dog",
        "Cat"
    ]
    result = organize_animals(animal_data, hierarchy)
    print(result)