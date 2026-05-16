def sort_by_category(data):
    return sorted(data, key=lambda x: (x['category'], x['name']))
if __name__ == '__main__':
    sample_data = [
        {'category': 'fruit', 'name': 'apple', 'value': 1.0},
        {'category': 'vegetable', 'name': 'carrot', 'value': 0.5},
        {'category': 'fruit', 'name': 'banana', 'value': 0.75},
        {'category': 'vegetable', 'name': 'broccoli', 'value': 1.2},
        {'category': 'fruit', 'name': 'orange', 'value': 0.9},
    ]
    sorted_data = sort_by_category(sample_data)
    for item in sorted_data:
        print(item)