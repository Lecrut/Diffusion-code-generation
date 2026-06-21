def create_sample_items():
    return [
        {"id": 1, "name": "apple", "type": "fruit"},
        {"id": 2, "name": "banana", "type": "fruit"},
        {"id": 3, "name": "cherry", "type": "fruit"},
        {"id": 4, "name": "date", "type": "fruit"},
        {"id": 5, "name": "elderberry", "type": "fruit"}
    ]

if __name__ == '__main__':
    items = create_sample_items()
    for item in items:
        print(f"ID: {item['id']}, Name: {item['name']}, Type: {item['type']}")