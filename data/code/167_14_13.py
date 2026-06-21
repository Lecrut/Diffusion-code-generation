stores = [
    {'name': 'Store A', 'age': 5},
    {'name': 'Store B', 'age': 12},
    {'name': 'Store C', 'age': 8}
]

def is_valid_store(store):
    return isinstance(store, dict) and 'name' in store and 'age' in store

def filter_stores(stores):
    if not all(is_valid_store(store) for store in stores):
        raise ValueError("All items in the list must be valid store dictionaries.")
    
    return [store for store in stores if store['age'] > 10]

if __name__ == '__main__':
    filtered_stores = filter_stores(stores)
    print(filtered_stores)