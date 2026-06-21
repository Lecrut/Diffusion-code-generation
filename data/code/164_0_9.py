def categorize_animals():
    animals = ['lion', 'eagle', 'snake', 'tiger', 'penguin', 'crocodile']
    category_mapping = {
        'mammal': ['lion', 'tiger'],
        'bird': ['eagle', 'penguin'],
        'reptile': ['snake', 'crocodile']
    }
    
    categorized_animals = {category: [] for category in category_mapping}
    
    for animal in animals:
        for category, species in category_mapping.items():
            if animal in species:
                categorized_animals[category].append(animal)
                break
    
    return categorized_animals

if __name__ == '__main__':
    result = categorize_animals()
    print(result)