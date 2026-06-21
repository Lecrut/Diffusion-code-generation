def create_items():
    return [
        {'id': 1, 'name': 'Apple', 'price': 0.99},
        {'id': 2, 'name': 'Banana', 'price': 0.59},
        {'id': 3, 'name': 'Cherry', 'price': 2.49}
    ]

if __name__ == '__main__':
    items = create_items()
    for item in items:
        print(item)