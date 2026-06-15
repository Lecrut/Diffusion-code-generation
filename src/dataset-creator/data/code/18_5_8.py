def classify_fruits(fruit_list):
    classification_map = {
        'Berry': ['strawberry', 'blueberry', 'raspberry', 'blackberry'],
        'Citrus': ['orange', 'lemon', 'lime', 'grapefruit'],
        'Pome': ['apple', 'pear', 'plum'],
        'Melon': ['watermelon', 'cantaloupe', 'honeydew'],
        'Drupe': ['peach', 'apricot', 'cherry'],
        'Banana': ['banana']
    }
    grouped_fruits = {}
    for fruit in fruit_list:
        found = False
        for category, fruits in classification_map.items():
            if fruit in fruits:
                if category not in grouped_fruits:
                    grouped_fruits[category] = []
                grouped_fruits[category].append(fruit)
                found = True
                break
        if not found:
            grouped_fruits['Other'] = [fruit]
    return grouped_fruits
if __name__ == '__main__':
    sample_fruits = [
        'apple', 'banana', 'orange', 'strawberry', 'grapefruit', 
        'pear', 'watermelon', 'peach', 'blueberry', 'lemon', 'plum'
    ]
    result = classify_fruits(sample_fruits)
    print(result)