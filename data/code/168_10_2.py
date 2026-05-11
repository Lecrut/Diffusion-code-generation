def categorize_items(items, mapping):
    grouped = {}
    for item in items:
        category = mapping.get(item, "Uncategorized")
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item)
    return grouped
if __name__ == '__main__':
    sample_items = [
        "apple",
        "banana",
        "carrot",
        "orange",
        "grape",
        "broccoli",
        "kiwi"
    ]
    category_mapping = {
        "apple": "Fruit",
        "banana": "Fruit",
        "orange": "Fruit",
        "grape": "Fruit",
        "carrot": "Vegetable",
        "broccoli": "Vegetable",
        "kiwi": "Fruit"
    }
    result = categorize_items(sample_items, category_mapping)
    for category, items in result.items():
        print(f"{category}: {items}")