ANIMAL_CATEGORIES = {
    'mammal': ['dog', 'cat', 'lion', 'elephant'],
    'bird': ['bird', 'penguin'],
    'reptile': ['snake', 'turtle']
}

def categorize_animals(animal_list):
    categorized_dict = {}
    for animal in animal_list:
        for category, animals in ANIMAL_CATEGORIES.items():
            if animal.lower() in animals:
                categorized_dict[animal] = category
                break
    return categorized_dict

if __name__ == '__main__':
    sample_animals = ["dog", "cat", "bird", "fish", "lion", "elephant", "snake", "turtle"]
    result = categorize_animals(sample_animals)
    print(result)