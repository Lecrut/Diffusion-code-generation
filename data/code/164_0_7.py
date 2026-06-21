def categorize_animals(animal_list):
    category_map = {
        'mammal': ['lion', 'tiger', 'elephant'],
        'bird': ['eagle', 'sparrow', 'penguin'],
        'reptile': ['snake', 'lizard', 'turtle']
    }
    
    categorized_animals = {category: [] for category in category_map}
    
    for animal in animal_list:
        for category, animals in category_map.items():
            if animal in animals:
                categorized_animals[category].append(animal)
                break
    
    return categorized_animals

if __name__ == '__main__':
    sample_animals = ['lion', 'eagle', 'snake', 'tiger', 'penguin']
    print(categorize_animals(sample_animals))