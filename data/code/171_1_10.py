def get_store_lengths(store_names):
    store_lengths = {}
    for name in store_names:
        lower_name = name.lower()
        if lower_name not in store_lengths:
            store_lengths[lower_name] = len(name)
    return store_lengths

if __name__ == '__main__':
    sample_stores = ["Apple Store", "Best Buy", "apple store", "Target"]
    print(get_store_lengths(sample_stores))