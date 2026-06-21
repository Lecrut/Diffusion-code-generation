def categorize_animals_by_locomotion(animals):
    locomotion_categories = {
        'swimming': [],
        'flying': [],
        'walking': []
    }
    
    for animal, locomotion in animals.items():
        if locomotion == 'swimming':
            locomotion_categories['swimming'].append(animal)
        elif locomotion == 'flying':
            locomotion_categories['flying'].append(animal)
        elif locomotion == 'walking':
            locomotion_categories['walking'].append(animal)
    
    return locomotion_categories

if __name__ == '__main__':
    sample_animals = {
        'Dolphin': 'swimming',
        'Eagle': 'flying',
        'Dog': 'walking',
        'Penguin': 'swimming',
        'Owl': 'flying',
        'Cat': 'walking'
    }
    
    categorized_animals = categorize_animals_by_locomotion(sample_animals)
    print(categorized_animals)