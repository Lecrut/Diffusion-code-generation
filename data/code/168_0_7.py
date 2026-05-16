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
        "dog",
        "cat",
        "broccoli",
        "fish",
        "milk"
    ]
    categorization_rule = {
        "fruits": lambda x: x.endswith("e"),
        "vegetables": lambda x: x in ["carrot", "broccoli"],
        "animals": lambda x: x in ["dog", "cat", "fish"],
        "dairy": lambda x: x == "milk"
    }
    result = categorize_items(sample_items, categorization_rule)
    print(result)