def classify_fruits(fruit_list):
    classification_map = {
        'Berry': ['strawberry', 'blueberry', 'raspberry', 'blackberry'],
        'Citrus': ['orange', 'lemon', 'lime', 'grapefruit'],
        'Pome': ['apple', 'pear', 'plum'],
        'Melon': ['watermelon', 'cantaloupe', 'honeydew'],
        'Drupe': ['peach', 'apricot', 'cherry'],
        'Grain': ['wheat', 'rice', 'barley']
    }
    grouped_fruits = {category: [] for category in classification_map}
    for fruit in fruit_list:
        found = False
        for category, fruits in classification_map.items():
            if fruit in fruits:
                grouped_fruits[category].append(fruit)
                found = True
                break
        if not found:
            pass
    return grouped_fruits
if __name__ == '__main__':
    sample_fruits = [
        'apple',
        'orange',
        'strawberry',
        'grapefruit',
        'pear',
        'watermelon',
        'peach',
        'lemon',
        'blueberry',
        'plum'
    ]
    result = classify_fruits(sample_fruits)
    for category, fruits in result.items():
        print(f"{category}: {fruits}")