def categorize_animals(animals):
    categories = {}
    for animal in animals:
        if ' ' in animal:
            type_, name = animal.split(' ', 1)
            if type_ not in categories:
                categories[type_] = []
            categories[type_].append(name)
    return categories

if __name__ == '__main__':
    sample_animals = ['Dog Max', 'Cat Whiskers', 'Bird Tweety', 'Fish Nemo', 'Dog Luna']
    categorized = categorize_animals(sample_animals)
    print(categorized)