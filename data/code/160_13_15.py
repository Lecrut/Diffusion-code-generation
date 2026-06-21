def initialize_inventory(item_names):
    if not all(isinstance(name, str) for name in item_names):
        raise ValueError("All items must be strings.")
    
    inventory = {}
    for item in set(item_names):
        inventory[item] = 1
    
    return inventory

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    inventory = initialize_inventory(sample_items)
    print(inventory)