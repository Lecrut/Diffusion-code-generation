def filter_stores(stores):
    if not isinstance(stores, list) or any(not isinstance(item, tuple) or len(item) != 2 for item in stores):
        raise ValueError("Input must be a list of tuples with two elements each.")
    
    return {name: desc for name, desc in stores if desc}

if __name__ == '__main__':
    sample_stores = [
        ("Store A", "A large retail location downtown."),
        ("Store B", ""),
        ("Store C", "A warehouse for electronics and gadgets."),
        ("Store D", None),
        ("Store E", "A specialty store for handmade goods.")
    ]
    
    filtered_stores = filter_stores(sample_stores)
    print(filtered_stores)