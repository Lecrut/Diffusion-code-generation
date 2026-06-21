def categorize_animals(animals):
    habitats = {
        'forest': ['Bear', 'Deer', 'Rabbit'],
        'ocean': ['Fish', 'Turtle', 'Octopus'],
        'desert': ['Camel', 'Lizard', 'Scorpion']
    }
    categorized = {habitat: [] for habitat in habitats}
    
    for animal, habitat in animals.items():
        if habitat in habitats:
            categorized[habitat].append(animal)
    
    return categorized

if __name__ == '__main__':
    sample_animals = {
        'Bear': 'forest',
        'Deer': 'forest',
        'Rabbit': 'forest',
        'Fish': 'ocean',
        'Turtle': 'ocean',
        'Octopus': 'ocean',
        'Camel': 'desert',
        'Lizard': 'desert',
        'Scorpion': 'desert'
    }
    
    result = categorize_animals(sample_animals)
    print(result)