def initialize_quantities(item_names):
    quantities = {}
    for item in set(item_names):
        quantities[item] = 1
    return quantities

if __name__ == '__main__':
    sample_items = [
        "apple",
        "banana",
        "pear",
        "orange",
        "kiwi"
    ]
    item_quantities = initialize_quantities(sample_items)
    print(item_quantities)