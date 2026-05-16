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
        "apple",
        "banana",
        "carrot",
        "orange",
        "broccoli",
        "grape",
        "spinach"
    ]
    categorization_rule = {
        "fruits": lambda x: x in ["apple", "banana", "orange", "grape"],
        "vegetables": lambda x: x in ["carrot", "broccoli", "spinach"],
        "other": lambda x: True
    }
    result = categorize_items(sample_items, categorization_rule)
    print(result)