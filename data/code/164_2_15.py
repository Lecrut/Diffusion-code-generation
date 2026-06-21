def categorize_animals(animals):
    categories = {'forest': [], 'ocean': [], 'desert': []}
    for animal in animals:
        if 'forest' in animal['habitat']:
            categories['forest'].append(animal)
        elif 'ocean' in animal['habitat']:
            categories['ocean'].append(animal)
        elif 'desert' in animal['habitat']:
            categories['desert'].append(animal)
    return categories

if __name__ == '__main__':
    animals = [
        {'name': 'Lion', 'habitat': 'forest'},
        {'name': 'Turtle', 'habitat': 'ocean'},
        {'name': 'Camel', 'habitat': 'desert'}
    ]
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)