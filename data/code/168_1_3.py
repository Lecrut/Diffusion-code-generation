def group_items_by_category(data):
    grouped = {}
    for item in data:
        category = item.get('category')
        if category:
            if category not in grouped:
                grouped[category] = []
            grouped[category].append(item)
    return grouped
if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'category': 'Fruit', 'price': 1.00},
        {'name': 'Carrot', 'category': 'Vegetable', 'price': 0.50},
        {'name': 'Banana', 'category': 'Fruit', 'price': 0.75},
        {'name': 'Broccoli', 'category': 'Vegetable', 'price': 1.20},
        {'name': 'Orange', 'category': 'Fruit', 'price': 0.99},
        {'name': 'Spinach', 'category': 'Vegetable', 'price': 2.50},
        {'name': 'Grape', 'category': 'Fruit', 'price': 3.00},
    ]
    result = group_items_by_category(sample_data)
    print(result)