def convert_tuples_to_dict(store_data):
    result = {}
    for store_name, age in store_data:
        result[store_name] = age
    return result

if __name__ == '__main__':
    sample_data = [
        ("StoreA", 30),
        ("StoreB", 25),
        ("StoreC", 35),
        ("StoreD", 28)
    ]
    processed_data = convert_tuples_to_dict(sample_data)
    print(processed_data)