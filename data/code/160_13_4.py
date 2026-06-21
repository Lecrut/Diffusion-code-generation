def initialize_item_quantities(item_names):
    return {item: 1 for item in set(item_names)}

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    quantities = initialize_item_quantities(sample_items)
    print(quantities)