def filter_keys(data_list, keys):
    return [{key: item[key] for key in keys if key in item} for item in data_list]

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Apple', 'price': 10, 'category': 'Fruit'},
        {'id': 2, 'name': 'Banana', 'price': 20, 'category': 'Fruit'},
        {'id': 3, 'name': 'Cherry', 'price': 30, 'category': 'Fruit'}
    ]
    keys_to_extract = ['id', 'name']
    filtered_data = filter_keys(sample_data, keys_to_extract)
    print(filtered_data)