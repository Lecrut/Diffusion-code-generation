def classify_fruits(fruit_list):
    classification_map = {
        'Berry': [],
        'Citrus': [],
        'Pome': [],
        'Drupe': [],
        'Melon': [],
        'Grain': [],
        'Other': []
    }
    for fruit in fruit_list:
        fruit_lower = fruit.lower()
        if 'berry' in fruit_lower or 'currant' in fruit_lower or 'raspberry' in fruit_lower:
            classification_map['Berry'].append(fruit)
        elif 'citrus' in fruit_lower or 'lemon' in fruit_lower or 'orange' in fruit_lower:
            classification_map['Citrus'].append(fruit)
        elif 'apple' in fruit_lower or 'pear' in fruit_lower:
            classification_map['Pome'].append(fruit)
        elif 'peach' in fruit_lower or 'plum' in fruit_lower:
            classification_map['Drupe'].append(fruit)
        elif 'melon' in fruit_lower or 'cantaloupe' in fruit_lower:
            classification_map['Melon'].append(fruit)
        elif 'wheat' in fruit_lower or 'rice' in fruit_lower:
            classification_map['Grain'].append(fruit)
        else:
            classification_map['Other'].append(fruit)
    return classification_map
if __name__ == '__main__':
    sample_fruits = [
        "Apple",
        "Orange",
        "Strawberry",
        "Banana",
        "Grape",
        "Lemon",
        "Pear",
        "Peach",
        "Watermelon",
        "Wheat",
        "Plum",
        "Cantaloupe"
    ]
    grouped_fruits = classify_fruits(sample_fruits)
    for classification, fruits in grouped_fruits.items():
        print(f"--- {classification} ---")
        if fruits:
            for fruit in fruits:
                print(f"- {fruit}")
        else:
            print("None found")