def initialize_item_list():
    return [
        {"name": "apple", "quantity": 10},
        {"name": "banana", "quantity": 20},
        {"name": "cherry", "quantity": 30},
        {"name": "date", "quantity": 40}
    ]

if __name__ == '__main__':
    item_list = initialize_item_list()
    print(item_list)