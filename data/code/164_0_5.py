def categorize_animals(animal_list):
    category_map = {
        'mammal': ['lion', 'tiger', 'elephant'],
        'bird': ['sparrow', 'eagle', 'penguin'],
        'reptile': ['snake', 'lizard', 'turtle']
    }
    categorized_animals = {}
    for animal in animal_list:
        found = False
        for category, animals in category_map.items():
            if animal in animals:
                if category not in categorized_animals:
                    categorized_animals[category] = []
                categorized_animals[category].append(animal)
                found = True
                break
        if not found:
            print(f"Unknown animal: {animal}")
    return categorized_animals

if __name__ == '__main__':
    animals = ['lion', 'sparrow', 'snake', 'rabbit', 'penguin']
    result = categorize_animals(animals)
    print(result)