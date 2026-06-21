def categorize_animals():
    animal_list = ["dog", "cat", "bird", "fish", "lion", "elephant"]
    category_map = {
        "mammal": ["dog", "cat", "lion", "elephant"],
        "bird": ["bird"],
        "reptile": ["fish"]
    }
    animal_dict = {}
    for animal in animal_list:
        for category, animals in category_map.items():
            if animal in animals:
                animal_dict[animal] = category
                break
    return animal_dict

if __name__ == '__main__':
    organized_data = categorize_animals()
    print(organized_data)