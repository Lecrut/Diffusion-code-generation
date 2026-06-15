def organize_data(data):
    organized = {}
    for item in data:
        category = item.get('category', 'uncategorized')
        if category not in organized:
            organized[category] = []
        organized[category].append(item)
    return organized
if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'category': 'fruit', 'color': 'red'},
        {'name': 'Carrot', 'category': 'vegetable', 'color': 'orange'},
        {'name': 'Banana', 'category': 'fruit', 'color': 'yellow'},
        {'name': 'Broccoli', 'category': 'vegetable', 'color': 'green'},
        {'name': 'Grape', 'category': 'fruit', 'color': 'purple'},
        {'name': 'Spinach', 'category': 'vegetable', 'color': 'green'},
        {'name': 'Car', 'category': 'transport', 'type': 'car'},
    ]
    result = organize_data(sample_data)
    import json
    print(json.dumps(result, indent=4))