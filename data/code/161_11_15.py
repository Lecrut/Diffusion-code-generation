def initialize_item_list() -> list:
    items = [
        {"name": "apple", "quantity": 10},
        {"name": "banana", "quantity": 20},
        {"name": "cherry", "quantity": 30}
    ]
    return items

if __name__ == '__main__':
    sample_items = initialize_item_list()
    print(sample_items)