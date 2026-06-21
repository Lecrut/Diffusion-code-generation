def categorize_animals(animals):
    categories = {
        'forest': [],
        'ocean': [],
        'desert': []
    }
    for animal, details in animals.items():
        habitat = details.get('habitat')
        if habitat in categories:
            categories[habitat].append(animal)
        else:
            raise ValueError(f"Invalid habitat: {habitat}")
    return categories

if __name__ == '__main__':
    sample_animals = {
        'Lion': {'age': 5, 'breed': 'African', 'habitat': 'forest'},
        'Turtle': {'age': 100, 'species': 'Green turtle', 'habitat': 'ocean'},
        'Camel': {'age': 20, 'breed': 'Dromedary', 'habitat': 'desert'},
        'Penguin': {'age': 3, 'species': 'Emperor penguin', 'habitat': 'ocean'}
    }
    categorized_animals = categorize_animals(sample_animals)
    print(categorized_animals)