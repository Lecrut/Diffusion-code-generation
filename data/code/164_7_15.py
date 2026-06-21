def categorize_animals_by_locomotion(animals):
    categories = {
        'swimming': [],
        'flying': [],
        'walking': []
    }
    for animal, locomotion in animals.items():
        if locomotion == 'swimming':
            categories['swimming'].append(animal)
        elif locomotion == 'flying':
            categories['flying'].append(animal)
        elif locomotion == 'walking':
            categories['walking'].append(animal)
    return categories

if __name__ == '__main__':
    animals = {
        'shark': 'swimming',
        'eagle': 'flying',
        'lion': 'walking',
        'penguin': 'swimming',
        'bat': 'flying'
    }
    categorized_animals = categorize_animals_by_locomotion(animals)
    print(categorized_animals)