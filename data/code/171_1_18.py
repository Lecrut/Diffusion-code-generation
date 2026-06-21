def store_name_lengths(store_names):
    name_length_map = {}
    for name in store_names:
        normalized_name = name.lower()
        if normalized_name not in name_length_map:
            name_length_map[normalized_name] = len(name)
    return name_length_map

if __name__ == '__main__':
    sample_stores = ['Apple Store', 'Best Buy', 'apple store', 'Target']
    print(store_name_lengths(sample_stores))