def categorize_animals(animals):
    animal_dict = {
        "Mammal": ["Dog", "Cat"],
        "Bird": ["Bird", "Eagle"],
        "Fish": ["Fish", "Tuna"]
    }
    categorized_animals = {}
    for animal in animals:
        stripped_animal = animal.strip()
        if stripped_animal:
            for category, category_animals in animal_dict.items():
                if stripped_animal in category_animals:
                    if category not in categorized_animals:
                        categorized_animals[category] = []
                    categorized_animals[category].append(stripped_animal)
    return categorized_animals

if __name__ == '__main__':
    sample_input = ["Dog", "Cat", "Bird", "Fish"]
    result = categorize_animals(sample_input)
    print(result)