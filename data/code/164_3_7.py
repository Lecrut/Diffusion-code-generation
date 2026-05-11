def organize_animals(animal_data, hierarchy):
    organized = {}
    for animal, group in animal_data.items():
        current_level = animal
        path = []
        found = False
        for i in range(len(hierarchy)):
            if animal == hierarchy[i]:
                current_level = hierarchy[i]
                path.append(hierarchy[i])
                found = True
                break
        if found:
            organized.setdefault(hierarchy[0], set()).add(animal)
        else:
            organized.setdefault("Other", set()).add(animal)
    return organized
if __name__ == '__main__':
    animal_data = {
        "Dog": ["Mammal"],
        "Cat": ["Mammal"],
        "Whale": ["Mammal"],
        "Eagle": ["Bird"],
        "Parrot": ["Bird"],
        "Fish": ["Fish"],
        "Snake": ["Reptile"]
    }
    hierarchy = [
        "Mammal",
        "Bird",
        "Fish",
        "Reptile"
    ]
    result = organize_animals(animal_data, hierarchy)
    print(result)