ITEM_DEFAULT_QUANTITY = 1

def initialize_inventory(item_names):
    inventory = {}
    for item in item_names:
        inventory[item] = ITEM_DEFAULT_QUANTITY
    return inventory

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    inventory = initialize_inventory(sample_items)
    print(inventory)