def categorize_animals(animals):
    categories = {'forest': [], 'ocean': [], 'desert': []}
    for animal in animals:
        if 'forest' in animal.lower():
            categories['forest'].append(animal)
        elif 'ocean' in animal.lower():
            categories['ocean'].append(animal)
        elif 'desert' in animal.lower():
            categories['desert'].append(animal)
    return categories

if __name__ == '__main__':
    animals = ['Lion', 'Tiger', 'Elephant', 'Fish', 'Shark', 'Camel']
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)