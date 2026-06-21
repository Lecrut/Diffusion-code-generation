def categorize_animals(animals):
    locomotion_categories = {
        'swimming': [],
        'flying': [],
        'walking': []
    }
    for animal, method in animals.items():
        if method == 'swim':
            locomotion_categories['swimming'].append(animal)
        elif method == 'fly':
            locomotion_categories['flying'].append(animal)
        elif method == 'walk':
            locomotion_categories['walking'].append(animal)
    return locomotion_categories

if __name__ == '__main__':
    animals = {
        'Dolphin': 'swim',
        'Eagle': 'fly',
        'Lion': 'walk',
        'Salmon': 'swim',
        'Owl': 'fly'
    }
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)