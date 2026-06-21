def organize_animals(animals):
    categories = {
        'forest': [],
        'ocean': [],
        'desert': []
    }
    
    for animal, details in animals.items():
        habitat = details.get('habitat')
        if habitat in categories:
            categories[habitat].append((animal, details))
        else:
            raise ValueError(f"Invalid habitat: {habitat}")
    
    return categories

if __name__ == '__main__':
    sample_animals = {
        'Lion': {'age': 10, 'breed': 'African', 'habitat': 'forest'},
        'Turtle': {'age': 50, 'species': 'Green turtle', 'habitat': 'ocean'},
        'Camel': {'age': 20, 'breed': 'Dromedary', 'habitat': 'desert'},
        'Penguin': {'age': 3, 'species': 'Emperor penguin', 'habitat': 'ocean'}
    }
    
    categorized_animals = organize_animals(sample_animals)
    print(categorized_animals['forest'])
    print(categorized_animals['ocean'])
    print(categorized_animals['desert'])