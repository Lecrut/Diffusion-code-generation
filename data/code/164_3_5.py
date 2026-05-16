def organize_animals(animal_data, hierarchy):
    organized = {}
    for animal, parent in animal_data.items():
        current_level = parent
        path = []
        while current_level:
            path.append(current_level)
            if current_level in hierarchy:
                current_level = hierarchy[current_level]
            else:
                break
        if path:
            for i in range(len(path) - 1):
                parent_node = path[i]
                child_node = path[i+1]
                if parent_node not in organized:
                    organized[parent_node] = []
                organized[parent_node].append(child_node)
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
        "Animal": "Reptile",
        "Reptile": "Snake"
    }
    result = organize_animals(animal_data, hierarchy)
    print(result)