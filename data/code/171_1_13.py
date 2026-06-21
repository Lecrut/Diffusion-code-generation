def map_store_names_to_lengths(store_names):
    store_lengths = {}
    for name in store_names:
        normalized_name = name.lower()
        if normalized_name not in store_lengths:
            store_lengths[normalized_name] = len(name)
    return store_lengths

if __name__ == '__main__':
    sample_stores = ["Apple Store", "Best Buy", "Walmart", "Target"]
    print(map_store_names_to_lengths(sample_stores))