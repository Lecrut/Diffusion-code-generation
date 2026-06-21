def generate_sample_items():
    items = [
        {'id': 1, 'name': 'apple', 'type': 'fruit'},
        {'id': 2, 'name': 'banana', 'type': 'fruit'},
        {'id': 3, 'name': 'cherry', 'type': 'fruit'},
        {'id': 4, 'name': 'date', 'type': 'fruit'},
        {'id': 5, 'name': 'elderberry', 'type': 'fruit'}
    ]
    return items

if __name__ == '__main__':
    sample_items = generate_sample_items()
    for item in sample_items:
        print(item)