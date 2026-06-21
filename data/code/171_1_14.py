def get_store_lengths(store_names):
    if not isinstance(store_names, list) or not all(isinstance(name, str) for name in store_names):
        raise ValueError("Input must be a list of strings")
    
    store_lengths = {}
    for name in store_names:
        normalized_name = name.lower()
        if normalized_name not in store_lengths:
            store_lengths[normalized_name] = len(normalized_name)
    
    return store_lengths

if __name__ == '__main__':
    sample_stores = ["Apple Store", "Banana Market", "apple store"]
    print(get_store_lengths(sample_stores))