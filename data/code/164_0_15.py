def categorize_animals():
    animals = ['lion', 'eagle', 'snake']
    categories = {
        'mammal': ['lion'],
        'bird': ['eagle'],
        'reptile': ['snake']
    }
    
    categorized_animals = {category: [] for category in categories}
    
    for animal in animals:
        for category, members in categories.items():
            if animal in members:
                categorized_animals[category].append(animal)
                break
    
    return categorized_animals

if __name__ == '__main__':
    result = categorize_animals()
    print(result)