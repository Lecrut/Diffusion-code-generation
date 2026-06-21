def filter_and_map_stores(store_data):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in store_data):
        raise ValueError("Input must be a list of tuples with two elements each.")
    
    return {name: description for name, description in store_data if description}

if __name__ == '__main__':
    stores = [
        ("Store A", "A large retail location downtown."),
        ("Store B", ""),
        ("Store C", "A warehouse for electronics and gadgets."),
        ("Store D", None)
    ]
    
    filtered_stores = filter_and_map_stores(stores)
    print(filtered_stores)