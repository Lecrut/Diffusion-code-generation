def categorize_animals(animals):
    categories = {
        'swimming': [],
        'flying': [],
        'walking': []
    }
    for animal in animals:
        if 'fish' in animal.lower():
            categories['swimming'].append(animal)
        elif 'bird' in animal.lower() or 'wing' in animal.lower():
            categories['flying'].append(animal)
        else:
            categories['walking'].append(animal)
    return categories

if __name__ == '__main__':
    sample_animals = ["Dog", "Cat", "Fish", "Bird", "Eagle", "Turtle"]
    categorized_animals = categorize_animals(sample_animals)
    print(categorized_animals)