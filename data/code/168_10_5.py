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
            categories["uncategorized"] = categories.get("uncategorized", [])
            categories["uncategorized"].append(item)
    return categories
if __name__ == '__main__':
    sample_items = ["apple", "banana", "carrot", "grape", "orange", "lettuce", "potato"]
    category_mapping = {
        "fruit": "apple",
        "fruit": "banana",
        "vegetable": "carrot",
        "vegetable": "lettuce",
        "fruit": "grape",
        "vegetable": "potato"
    }
    result = categorize_items(sample_items, category_mapping)
    print(result)