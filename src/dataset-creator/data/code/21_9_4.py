def organize_data(data):
    organized = {}
    for item in data:
        if 'category' in item:
            category = item['category']
            if category not in organized:
                organized[category] = []
            organized[category].append(item)
        else:
            default_category = 'uncategorized'
            if default_category not in organized:
                organized[default_category] = []
            organized[default_category].append(item)
    return organized
if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'category': 'fruit', 'value': 10},
        {'name': 'Carrot', 'category': 'vegetable', 'value': 5},
        {'name': 'Banana', 'category': 'fruit', 'value': 8},
        {'name': 'Broccoli', 'category': 'vegetable', 'value': 12},
        {'name': 'Milk', 'category': 'dairy', 'value': 3},
        {'name': 'Orange', 'category': 'fruit', 'value': 15},
        {'name': 'Rice', 'category': 'grain', 'value': 7},
        {'name': 'Cheese', 'category': 'dairy', 'value': 9}
    ]
    result = organize_data(sample_data)
    import json
    print(json.dumps(result, indent=4))