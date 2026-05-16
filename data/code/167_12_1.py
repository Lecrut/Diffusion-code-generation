def process_store_data(data):
    result = {}
    for store_name, age in data:
        result[store_name] = age
    return result
if __name__ == '__main__':
    sample_data = [
        ("StoreA", 10),
        ("StoreB", 25),
        ("StoreC", 5),
        ("StoreD", 30)
    ]
    processed_data = process_store_data(sample_data)
    print(processed_data)