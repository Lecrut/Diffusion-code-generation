def categorize_animals(animals):
    categories = {
        'forest': [],
        'ocean': [],
        'desert': []
    }
    
    for animal, habitat in animals.items():
        if habitat in categories:
            categories[habitat].append(animal)
    
    return categories

if __name__ == '__main__':
    sample_animals = {
        'lion': 'forest',
        'tiger': 'forest',
        'shark': 'ocean',
        'dolphin': 'ocean',
        'camel': 'desert',
        'snake': 'desert'
    }
    
    categorized_animals = categorize_animals(sample_animals)
    print(categorized_animals)