def categorize_items(items, rule):
    categories = {}
    for item in items:
        category = None
        for cat, condition in rule.items():
            if condition(item):
                category = cat
                break
        if category is not None:
            if category not in categories:
                categories[category] = []
            categories[category].append(item)
        else:
            categories['uncategorized'] = categories.get('uncategorized', [])
            categories['uncategorized'].append(item)
    return categories
if __name__ == '__main__':
    sample_items = [
        "Apple",
        "Carrot",
        "Banana",
        "Broccoli",
        "Orange",
        "Potato",
        "Grape",
        "Spinach"
    ]
    categorization_rule = {
        "Vegetables": lambda x: x in ["Carrot", "Broccoli", "Potato", "Spinach"],
        "Fruits": lambda x: x in ["Apple", "Banana", "Orange", "Grape"]
    }
    result = categorize_items(sample_items, categorization_rule)
    print(result)