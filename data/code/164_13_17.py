def sort_animals_by_category(animals):
    animal_categories = {
        "mammals": ["Dog", "Cat"],
        "birds": ["Bird"],
        "fish": ["Fish"]
    }
    
    categorized_animals = {category: [] for category in animal_categories}
    
    for animal in animals:
        if animal in animal_categories["mammals"]:
            categorized_animals["mammals"].append(animal)
        elif animal in animal_categories["birds"]:
            categorized_animals["birds"].append(animal)
        elif animal in animal_categories["fish"]:
            categorized_animals["fish"].append(animal)
    
    return categorized_animals

if __name__ == '__main__':
    sample_animals = [
        "Dog",
        "cat",
        "Bird",
        123,
        "fish",
        "Dog"
    ]
    
    sorted_animals = sort_animals_by_category(sample_animals)
    print(sorted_animals)