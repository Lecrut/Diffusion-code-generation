def initialize_item_list() -> list[dict]:
    return [
        {"id": 1, "name": "apple", "quantity": 3},
        {"id": 2, "name": "banana", "quantity": 5},
        {"id": 3, "name": "cherry", "quantity": 7}
    ]

if __name__ == '__main__':
    item_list = initialize_item_list()
    print(item_list)