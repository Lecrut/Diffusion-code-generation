def validate_store_names(store_names):
    if not isinstance(store_names, list) or not all(isinstance(name, str) for name in store_names):
        raise ValueError("Input must be a list of strings")

def get_store_name_lengths(store_names):
    validate_store_names(store_names)
    return {name.lower(): len(name) for name in store_names}

if __name__ == '__main__':
    sample_stores = ["Apple Store", "Best Buy", "Target"]
    print(get_store_name_lengths(sample_stores))