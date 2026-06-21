ITEM_FIELDS = [
    "name",
    "quantity",
    "price"
]

SAMPLE_ITEMS = [
    {"name": "apple", "quantity": 42, "price": 1.50},
    {"name": "banana", "quantity": 99, "price": 0.75},
    {"name": "cherry", "quantity": 101, "price": 3.00},
    {"name": "date", "quantity": 55, "price": 2.50},
    {"name": "elderberry", "quantity": 200, "price": 4.00}
]

def get_sample_item_list():
    return SAMPLE_ITEMS

if __name__ == '__main__':
    sample_items = get_sample_item_list()
    print("Sample Item List:")
    for index, item in enumerate(sample_items):
        print(f"{index + 1}. {item}")