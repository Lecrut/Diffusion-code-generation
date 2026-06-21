def categorize_animals(animal_list):
    animal_dict = {
        "mammal": ["dog", "cat", "lion", "elephant", "tiger"],
        "bird": ["bird", "sparrow", "eagle"],
        "reptile": ["snake", "lizard", "turtle"]
    }
    
    categorized_animals = {}
    for animal in animal_list:
        for category, animals in animal_dict.items():
            if animal in animals:
                categorized_animals[animal] = category
                break
    
    return categorized_animals

if __name__ == '__main__':
    sample_animals = ["dog", "bird", "snake", "fish"]
    organized_data = categorize_animals(sample_animals)
    print(organized_data)