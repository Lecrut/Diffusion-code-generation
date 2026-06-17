def filter_items(items):
    return [item for item in items if item.get('key') == 'target_value']
if __name__ == '__main__':
    data = [
        {'id': 1, 'key': 'source'},
        {'id': 2, 'key': 'target_value'},
        {'id': 3, 'key': 'other'},
        {'id': 4, 'key': 'target_value'}
    ]
    result = filter_items(data)
    for item in result:
        print(item['id'])