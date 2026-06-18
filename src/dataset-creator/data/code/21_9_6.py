def organize_data(data_list):
    organized_data = {}
    for item in data_list:
        if 'category' in item:
            category = item['category']
            if category not in organized_data:
                organized_data[category] = []
            organized_data[category].append(item)
        else:
            default_category = 'uncategorized'
            if default_category not in organized_data:
                organized_data[default_category] = []
            organized_data[default_category].append(item)
    return organized_data
if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'category': 'Fruit', 'value': 10},
        {'name': 'Carrot', 'category': 'Vegetable', 'value': 5},
        {'name': 'Banana', 'category': 'Fruit', 'value': 8},
        {'name': 'Broccoli', 'category': 'Vegetable', 'value': 12},
        {'name': 'Milk', 'category': 'Dairy', 'value': 4},
        {'name': 'Orange', 'category': 'Fruit', 'value': 9},
        {'name': 'Rice', 'category': 'Grain', 'value': 6},
        {'name': 'Cheese', 'category': 'Dairy', 'value': 7},
        {'name': 'Potato', 'category': 'Vegetable', 'value': 5},
        {'name': 'Water', 'category': 'Beverage', 'value': 3}
    ]
    result = organize_data(sample_data)
    for category, items in result.items():
        print(f"--- {category} ---")
        for item in items:
            print(f"Name: {item['name']}, Value: {item['value']}")
        print()