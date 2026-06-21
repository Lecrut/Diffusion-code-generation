def initialize_inventory(item_names):
    return {item: 1 for item in item_names}

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    inventory = initialize_inventory(sample_items)
    print(inventory)