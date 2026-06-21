def store_name_lengths(store_names):
    lengths = {}
    for name in store_names:
        lower_name = name.lower()
        if lower_name not in lengths:
            lengths[lower_name] = len(name)
    return lengths

if __name__ == '__main__':
    sample_stores = ["Apple Store", "Best Buy", "apple store", "Tech City"]
    print(store_name_lengths(sample_stores))