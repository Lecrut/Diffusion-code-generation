def create_sample_items():
    return [
        {"id": 1, "name": "apple", "quantity": 42},
        {"id": 2, "name": "banana", "quantity": 99},
        {"id": 3, "name": "cherry", "quantity": 101},
        {"id": 4, "name": "date", "quantity": 55},
        {"id": 5, "name": "elderberry", "quantity": 200}
    ]

if __name__ == '__main__':
    items = create_sample_items()
    for item in items:
        print(item)