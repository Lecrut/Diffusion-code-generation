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
        {'name': 'Apple', 'category': 'Fruit', 'price': 1.00},
        {'name': 'Carrot', 'category': 'Vegetable', 'price': 0.50},
        {'name': 'Banana', 'category': 'Fruit', 'price': 0.75},
        {'name': 'Broccoli', 'category': 'Vegetable', 'price': 1.20},
        {'name': 'Orange', 'category': 'Fruit', 'price': 0.99},
        {'name': 'Potato', 'category': 'Vegetable', 'price': 0.40},
        {'name': 'Grape', 'category': 'Fruit', 'price': 2.50}
    ]
    grouped_data = group_items_by_category(sample_data)
    print(grouped_data)