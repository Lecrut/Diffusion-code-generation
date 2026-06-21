def initialize_item_list() -> list[dict]:
    return [
        {"id": 1, "name": "apple", "category": "fruit"},
        {"id": 2, "name": "banana", "category": "fruit"},
        {"id": 3, "name": "cherry", "category": "fruit"},
        {"id": 4, "name": "date", "category": "fruit"}
    ]

if __name__ == '__main__':
    sample_list = initialize_item_list()
    print(sample_list)