def sort_by_category(data):
    return sorted(data, key=lambda x: (x['category'], x['name']))
if __name__ == '__main__':
    sample_data = [
        {'category': 'A', 'name': 'Banana', 'value': 10},
        {'category': 'B', 'name': 'Apple', 'value': 5},
        {'category': 'A', 'name': 'Cherry', 'value': 12},
        {'category': 'B', 'name': 'Orange', 'value': 8},
        {'category': 'A', 'name': 'Avocado', 'value': 15},
        {'category': 'C', 'name': 'Grape', 'value': 20},
    ]
    sorted_data = sort_by_category(sample_data)
    for item in sorted_data:
        print(item)