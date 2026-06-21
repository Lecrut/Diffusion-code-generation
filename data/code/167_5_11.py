def validate_data(data):
    if not isinstance(data, list) or len(data) != 5:
        raise ValueError("Data must be a list of exactly five tuples.")
    for item in data:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Each item in the list must be a tuple of two elements.")
        store_name, age = item
        if not isinstance(store_name, str) or not isinstance(age, int):
            raise ValueError("First element of each tuple must be a string and second an integer.")

def create_store_dict(data):
    validate_data(data)
    return {store_name: age for store_name, age in data}

if __name__ == '__main__':
    sample_data = [
        ("StoreA", 30),
        ("StoreB", 25),
        ("StoreC", 40),
        ("StoreD", 35),
        ("StoreE", 28)
    ]
    store_dict = create_store_dict(sample_data)
    print(store_dict)