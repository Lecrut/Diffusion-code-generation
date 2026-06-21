def categorize_animals():
    animals = ['lion', 'eagle', 'snake', 'tiger', 'penguin', 'crocodile']
    category_map = {
        'mammal': ['lion', 'tiger'],
        'bird': ['eagle', 'penguin'],
        'reptile': ['snake', 'crocodile']
    }
    
    categorized_animals = {category: [] for category in category_map}
    
    for animal in animals:
        for category, species in category_map.items():
            if animal in species:
                categorized_animals[category].append(animal)
                break
    
    return categorized_animals

if __name__ == '__main__':
    result = categorize_animals()
    print(result)