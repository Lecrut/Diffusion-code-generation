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
        'tiger': 'forest',
        'shark': 'ocean',
        'camel': 'desert',
        'lion': 'forest',
        'dolphin': 'ocean',
        'rabbit': 'forest'
    }
    categorized_animals = categorize_animals(sample_animals)
    print(categorized_animals)