def filter_stores(stores):
    if not isinstance(stores, list) or not all(isinstance(store, tuple) and len(store) == 2 for store in stores):
        raise ValueError("Input must be a list of tuples with two elements each.")
    
    return {name: description for name, description in stores if description}

if __name__ == '__main__':
    sample_stores = [
        ("Store A", "A large retail location downtown."),
        ("Store B", ""),
        ("Store C", "A warehouse for electronics and gadgets."),
        ("Store D", None)
    ]
    
    filtered_stores = filter_stores(sample_stores)
    print(filtered_stores)