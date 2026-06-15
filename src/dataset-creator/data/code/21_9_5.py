def organize_data(data_list):
    organized_data = {}
    for item in data_list:
        group_key = None
        if 'category' in item:
            group_key = item['category']
        elif 'level1' in item:
            group_key = item['level1']
        if group_key:
            if group_key not in organized_data:
                organized_data[group_key] = []
            organized_data[group_key].append(item)
        else:
            default_key = "uncategorized"
            if default_key not in organized_data:
                organized_data[default_key] = []
            organized_data[default_key].append(item)
    return organized_data
if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'category': 'Fruit', 'level1': 'Produce'},
        {'name': 'Carrot', 'category': 'Vegetable', 'level1': 'Produce'},
        {'name': 'Banana', 'category': 'Fruit', 'level1': 'Produce'},
        {'name': 'Broccoli', 'category': 'Vegetable', 'level1': 'Produce'},
        {'name': 'Milk', 'category': 'Dairy', 'level1': 'Dairy'},
        {'name': 'Cheese', 'category': 'Dairy', 'level1': 'Dairy'},
        {'name': 'Rice', 'category': 'Grain', 'level1': 'Grains'},
        {'name': 'Potato', 'category': 'Vegetable', 'level1': 'Starchy'},
        {'name': 'Water', 'category': 'Beverage'},
    ]
    result = organize_data(sample_data)
    print(result)