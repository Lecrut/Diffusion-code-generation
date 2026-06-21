def categorize_animals(animals):
    categories = {}
    for animal in animals:
        category = animal.split()[0]
        if category not in categories:
            categories[category] = []
        categories[category].append(animal)
    return categories

if __name__ == '__main__':
    sample_animals = ['Dog Spot', 'Cat Whiskers', 'Bird Tweety', 'Fish Nemo', 'Dog Max']
    categorized_animals = categorize_animals(sample_animals)
    print(categorized_animals)