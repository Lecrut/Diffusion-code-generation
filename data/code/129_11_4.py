def sort_by_category(data):
    return sorted(data, key=lambda x: (x['category'], x['name']))
if __name__ == '__main__':
    sample_data = [
        {'category': 'Fruit', 'name': 'Apple', 'value': 1.0},
        {'category': 'Vegetable', 'name': 'Carrot', 'value': 0.5},
        {'category': 'Fruit', 'name': 'Banana', 'value': 0.75},
        {'category': 'Vegetable', 'name': 'Broccoli', 'value': 1.2},
        {'category': 'Fruit', 'name': 'Orange', 'value': 0.9},
    ]
    sorted_data = sort_by_category(sample_data)
    for item in sorted_data:
        print(item)