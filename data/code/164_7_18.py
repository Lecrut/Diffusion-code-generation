def categorize_animals(animals):
    categories = {'swimming': [], 'flying': [], 'walking': []}
    for animal in animals:
        if 'fish' in animal.lower():
            categories['swimming'].append(animal)
        elif 'bird' in animal.lower() or 'fly' in animal.lower():
            categories['flying'].append(animal)
        elif 'walk' in animal.lower() or 'run' in animal.lower():
            categories['walking'].append(animal)
    return categories

if __name__ == '__main__':
    sample_animals = ["Dog", "Cat", "Bird", "Fish", "Eagle", "Turtle"]
    categorized_animals = categorize_animals(sample_animals)
    print(f"Categorized Animals: {categorized_animals}")