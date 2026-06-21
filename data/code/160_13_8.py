def initialize_inventory(item_names):
    inventory = {}
    for item in item_names:
        if item not in inventory:
            inventory[item] = 1
    return inventory

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry', 'apple']
    inventory = initialize_inventory(sample_items)
    print(inventory)