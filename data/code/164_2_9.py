def categorize_animals(animals):
    categories = {
        'forest': [],
        'ocean': [],
        'desert': []
    }
    
    for animal, details in animals.items():
        if 'habitat' in details:
            habitat = details['habitat']
            if habitat in categories:
                categories[habitat].append(animal)
    
    return categories

if __name__ == '__main__':
    animals = {
        "Lion": {"age": 5, "breed": "African", "habitat": "forest"},
        "Dolphin": {"age": 3, "species": "Bottlenose", "habitat": "ocean"},
        "Camel": {"age": 7, "breed": "Arabian", "habitat": "desert"},
        "Penguin": {"age": 2, "species": "Emperor", "habitat": "ocean"}
    }
    
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)