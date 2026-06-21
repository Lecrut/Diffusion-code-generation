def initialize_inventory(item_names):
    if not isinstance(item_names, list) or not all(isinstance(item, str) for item in item_names):
        raise ValueError("Input must be a list of strings")
    
    return {item: 1 for item in set(item_names)}

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    inventory = initialize_inventory(sample_items)
    print(inventory)