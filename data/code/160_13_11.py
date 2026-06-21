INITIAL_QUANTITY = 1

def initialize_inventory(item_names):
    return {item: INITIAL_QUANTITY for item in set(item_names)}

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    inventory = initialize_inventory(sample_items)
    print(inventory)