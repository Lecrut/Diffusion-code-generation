ITEM_LIST = [
    {"name": "apple", "category": "fruit", "price": 0.5},
    {"name": "banana", "category": "fruit", "price": 0.3},
    {"name": "cherry", "category": "fruit", "price": 1.2},
    {"name": "date", "category": "fruit", "price": 2.5}
]

def initialize_item_list() -> list:
    return ITEM_LIST

if __name__ == '__main__':
    initialized_list = initialize_item_list()
    print(initialized_list)