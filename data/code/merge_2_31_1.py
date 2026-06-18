def filter_items(items_list):
    return [item for item in items_list if isinstance(item, dict) and item.get('key') == 'target_value']
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'key': 'exclude_me'},
        {'id': 2, 'key': 'target_value', 'value': 'data_1'},
        {'id': 3, 'key': 'another_exclude'},
        {'id': 4, 'key': 'target_value', 'value': 'data_2'}
    ]
    filtered = filter_items(sample_data)
    for item in filtered:
        print(item['id'], '-', item.get('value'))