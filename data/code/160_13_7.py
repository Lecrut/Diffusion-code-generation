ITEM_DEFAULT_QUANTITY = 1

def initialize_inventory(item_names):
    return {item: ITEM_DEFAULT_QUANTITY for item in item_names}

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    inventory = initialize_inventory(sample_items)
    print(inventory)