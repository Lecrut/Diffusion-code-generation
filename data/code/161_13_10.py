def get_sample_items():
    return [
        {'id': 1, 'name': 'Item A', 'description': 'Description for Item A'},
        {'id': 2, 'name': 'Item B', 'description': 'Description for Item B'},
        {'id': 3, 'name': 'Item C', 'description': 'Description for Item C'}
    ]

if __name__ == '__main__':
    sample_items = get_sample_items()
    print(sample_items)