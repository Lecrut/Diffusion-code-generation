from collections import namedtuple

def validate_store_data(data):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in data):
        raise ValueError("Data must be a list of tuples with exactly two elements each.")
    if not all(isinstance(store_name, str) for store_name, _ in data):
        raise ValueError("Store names must be strings.")
    if not all(isinstance(age, int) and age >= 0 for _, age in data):
        raise ValueError("Ages must be non-negative integers.")

def process_store_data(data):
    validate_store_data(data)
    StoreInfo = namedtuple('StoreInfo', ['name', 'age'])
    store_infos = [StoreInfo(name, age) for name, age in data]
    return store_infos

if __name__ == '__main__':
    sample_data = [
        ("StoreA", 10),
        ("StoreB", 25),
        ("StoreC", 30),
        ("StoreD", 15)
    ]
    processed_data = process_store_data(sample_data)
    for store_info in processed_data:
        print(store_info.name, store_info.age)