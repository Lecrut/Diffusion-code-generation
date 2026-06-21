def get_sample_items():
    return [
        {'id': 1, 'name': 'Apple', 'category': 'Fruit'},
        {'id': 2, 'name': 'Banana', 'category': 'Fruit'},
        {'id': 3, 'name': 'Carrot', 'category': 'Vegetable'}
    ]

if __name__ == '__main__':
    sample_items = get_sample_items()
    print(sample_items)