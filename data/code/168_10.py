def categorize_items(items, mapping):
    categories = {}
    for item in items:
        found = False
        for category, value in mapping.items():
            if item == value:
                if category not in categories:
                    categories[category] = []
                categories[category].append(item)
                found = True
                break
        if not found:
            default_category = "Uncategorized"
            if default_category not in categories:
                categories[default_category] = []
            categories[default_category].append(item)
    return categories
if __name__ == '__main__':
    sample_items = ["apple", "banana", "carrot", "grape", "orange", "broccoli", "kiwi", "spinach"]
    category_mapping = {
        "Fruit": "apple",
        "Fruit": "banana",
        "Vegetable": "carrot",
        "Vegetable": "broccoli",
        "Fruit": "grape",
        "Vegetable": "spinach"
    }
    result = categorize_items(sample_items, category_mapping)
    print(result)