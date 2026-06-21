def categorize_animals(animals):
    categorized = {}
    for animal in animals:
        if 'bird' in animal.lower():
            category = 'birds'
        elif 'mammal' in animal.lower():
            category = 'mammals'
        else:
            category = 'other'
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(animal)
    return categorized

if __name__ == '__main__':
    sample_animals = ['Eagle', 'Lion', 'Penguin', 'Dog', 'Cat', 'Fish']
    print(categorize_animals(sample_animals))