def data_generator(data):
    for store_name, age in data:
        yield store_name, age
if __name__ == '__main__':
    sample_data = [
        ("StoreA", 30),
        ("StoreB", 25),
        ("StoreC", 40),
        ("StoreD", 22),
        ("StoreE", 35)
    ]
    generator = data_generator(sample_data)
    print("Starting data iteration:")
    for name, age in generator:
        print(f"Store: {name}, Age: {age}")