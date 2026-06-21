def categorize_animals_by_locomotion(animals):
    locomotion_categories = {
        'swimming': [],
        'flying': [],
        'walking': []
    }
    for animal, mode in animals.items():
        locomotion_categories[mode].append(animal)
    return locomotion_categories

if __name__ == '__main__':
    sample_animals = {
        'dolphin': 'swimming',
        'eagle': 'flying',
        'lion': 'walking',
        'penguin': 'swimming',
        'ostrich': 'walking'
    }
    categorized_animals = categorize_animals_by_locomotion(sample_animals)
    print(categorized_animals)