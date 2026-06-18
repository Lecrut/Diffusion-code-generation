def classify_fruits(fruit_list):
    classification_map = {
        'Berry': [],
        'Citrus': [],
        'Pome': [],
        'Drupe': [],
        'Melon': [],
        'Pear': [],
        'Fig': [],
        'Banana': []
    }
    fruit_categories = {
        "Apple": "Pome",
        "Orange": "Citrus",
        "Strawberry": "Berry",
        "Grape": "Berry",
        "Lemon": "Citrus",
        "Pear": "Pome",
        "Peach": "Drupe",
        "Mango": "Drupe",
        "Banana": "Berry"                                    
    }
    for fruit in fruit_list:
        if fruit in fruit_categories:
            category = fruit_categories[fruit]
            if category in classification_map:
                classification_map[category].append(fruit)
            else:
                print(f"Warning: Fruit {fruit} belongs to unmapped category {category}")
    return classification_map
if __name__ == '__main__':
    sample_fruits = [
        "Apple",
        "Orange",
        "Strawberry",
        "Grape",
        "Lemon",
        "Pear",
        "Peach",
        "Mango",
        "Banana"
    ]
    grouped_results = classify_fruits(sample_fruits)
    for category, fruits in grouped_results.items():
        print(f"{category}: {fruits}")