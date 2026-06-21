def categorize_animals(animals):
    categories = {'forest': [], 'ocean': [], 'desert': []}
    
    for animal, details in animals.items():
        if 'habitat' in details:
            habitat = details['habitat']
            if habitat in categories:
                categories[habitat].append(animal)
            else:
                raise ValueError(f"Invalid habitat: {habitat}")
        else:
            raise ValueError(f"Habitat not specified for animal: {animal}")
    
    return categories

if __name__ == '__main__':
    animals = {
        'Lion': {'age': 5, 'breed': 'African', 'habitat': 'desert'},
        'Elephant': {'age': 20, 'weight': '6 tons', 'habitat': 'forest'},
        'Turtle': {'age': 100, 'shell_color': 'green', 'habitat': 'ocean'},
        'Penguin': {'age': 3, 'species': 'Adelie', 'habitat': 'ocean'}
    }
    
    organized_animals = categorize_animals(animals)
    print(organized_animals)