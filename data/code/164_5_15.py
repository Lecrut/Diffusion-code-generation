def categorize_animals(animals):
    diet_categories = {
        'herbivore': ['Elephant', 'Giraffe'],
        'carnivore': ['Lion', 'Tiger', 'Bear'],
        'omnivore': ['Zebra', 'Monkey']
    }
    
    categorized_animals = {'herbivore': [], 'carnivore': [], 'omnivore': []}
    
    for animal in animals:
        for category, diets in diet_categories.items():
            if animal in diets:
                categorized_animals[category].append(animal)
                break
    
    return categorized_animals

if __name__ == '__main__':
    sample_animals = ["Lion", "Tiger", "Elephant", "Bear", "Zebra", "Giraffe", "Monkey"]
    result = categorize_animals(sample_animals)
    print(result)