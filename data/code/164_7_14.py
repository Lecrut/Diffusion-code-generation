def categorize_animals(animals):
    locomotion_categories = {
        'swimming': [],
        'flying': [],
        'walking': []
    }
    
    for animal in animals:
        if 'fish' in animal.lower():
            locomotion_categories['swimming'].append(animal)
        elif 'bird' in animal.lower() or 'winged' in animal.lower():
            locomotion_categories['flying'].append(animal)
        else:
            locomotion_categories['walking'].append(animal)
    
    return locomotion_categories

if __name__ == '__main__':
    animals = ["Dog", "Cat", "Bird", "Fish", "Penguin", "Owl", "Antelope"]
    categorized_animals = categorize_animals(animals)
    print(categorized_animals)