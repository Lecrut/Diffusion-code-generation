def categorize_animals(animals):
    animal_classifications = {
        "dog": "endothermic",
        "cat": "endothermic",
        "bird": "endothermic",
        "fish": "ectothermic",
        "lion": "endothermic",
        "cow": "endothermic"
    }
    categorized_animals = {"endothermic": [], "ectothermic": []}
    for animal in animals:
        if animal in animal_classifications:
            category = animal_classifications[animal]
            categorized_animals[category].append(animal)
    return categorized_animals

if __name__ == '__main__':
    sample_animals = ["dog", "cat", "bird", "fish", "lion", "cow"]
    organized_animals = categorize_animals(sample_animals)
    print(organized_animals)