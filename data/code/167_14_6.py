stores = [
    {'name': 'Store A', 'age': 5},
    {'name': 'Store B', 'age': 12},
    {'name': 'Store C', 'age': 8}
]

def validate_stores(stores):
    if not all(isinstance(store, dict) and 'name' in store and 'age' in store for store in stores):
        raise ValueError("Invalid stores data format")

def filter_stores(stores):
    validate_stores(stores)
    return [store for store in stores if store['age'] > 10]

if __name__ == '__main__':
    filtered_stores = filter_stores(stores)
    print(filtered_stores)