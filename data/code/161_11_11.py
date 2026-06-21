def initialize_item_list():
    items = [
        {'name': 'apple', 'quantity': 10, 'price_per_unit': 0.5},
        {'name': 'banana', 'quantity': 20, 'price_per_unit': 0.3},
        {'name': 'cherry', 'quantity': 15, 'price_per_unit': 0.8}
    ]
    return items

if __name__ == '__main__':
    sample_items = initialize_item_list()
    print(sample_items)