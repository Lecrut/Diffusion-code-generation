def group_items_by_category(data):
    result = {}
    for item in data:
        category = item.get('category')
        if category:
            if category not in result:
                result[category] = []
            result[category].append(item)
    return result
if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'category': 'Fruit', 'price': 1.0},
        {'name': 'Carrot', 'category': 'Vegetable', 'price': 0.5},
        {'name': 'Banana', 'category': 'Fruit', 'price': 0.75},
        {'name': 'Broccoli', 'category': 'Vegetable', 'price': 1.2},
        {'name': 'Orange', 'category': 'Fruit', 'price': 0.9},
        {'name': 'Spinach', 'category': 'Vegetable', 'price': 2.0}
    ]
    grouped_data = group_items_by_category(sample_data)
    print(grouped_data)