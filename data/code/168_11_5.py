def group_items(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_comprehension(data):
    grouped = {}
    for item in data:
        category = item['category']
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item['item'])
    return grouped
def group_items_optimized(data):
    return {category: [item['item'] for item in data if item['category'] == category] for category in set(item['category'] for item in data)}
if __name__ == '__main__':
    sample_data = [
        {'item': 'Apple', 'category': 'Fruit'},
        {'item': 'Carrot', 'category': 'Vegetable'},
        {'item': 'Banana', 'category': 'Fruit'},
        {'item': 'Broccoli', 'category': 'Vegetable'},
        {'item': 'Orange', 'category': 'Fruit'},
        {'item': 'Spinach', 'category': 'Vegetable'}
    ]
    result = group_items_optimized(sample_data)
    print(result)