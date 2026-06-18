def classify_fruits(fruit_list):
    classification_map = {
        'Berry': [],
        'Citrus': [],
        'Pome': [],
        'Drupe': [],
        'Melon': [],
        'Pear': [],
        'Fig': [],
        'Grape': []
    }
    fruit_categories = {
        "Apple": "Pome",
        "Banana": "Berry",
        "Orange": "Citrus",
        "Grape": "Berry",
        "Strawberry": "Berry",
        "Lemon": "Citrus",
        "Pear": "Pome",
        "Peach": "Drupe",
        "Plum": "Drupe",
        "Melon": "Melon",
        "Fig": "Fig"
    }
    for fruit in fruit_list:
        if fruit in fruit_categories:
            category = fruit_categories[fruit]
            if category in classification_map:
                classification_map[category].append(fruit)
            else:
                pass
    return classification_map
if __name__ == '__main__':
    sample_fruits = [
        "Apple",
        "Banana",
        "Orange",
        "Grape",
        "Strawberry",
        "Lemon",
        "Pear",
        "Peach",
        "Plum",
        "Melon",
        "Fig"
    ]
    grouped_fruits = classify_fruits(sample_fruits)
    for category, fruits in grouped_fruits.items():
        print(f"{category}: {fruits}")