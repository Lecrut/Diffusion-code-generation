ITEM_KEYS = ["name", "quantity", "price"]

def initialize_item_list():
    return [
        {"name": "apple", "quantity": 10, "price": 0.5},
        {"name": "banana", "quantity": 20, "price": 0.3},
        {"name": "cherry", "quantity": 15, "price": 0.8}
    ]

if __name__ == '__main__':
    item_list = initialize_item_list()
    print(item_list)