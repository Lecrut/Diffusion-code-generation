stores = [
    {'name': 'Store A', 'age': 5},
    {'name': 'Store B', 'age': 12},
    {'name': 'Store C', 'age': 8}
]

def is_store_eligible(store):
    return store['age'] > 10

def filter_stores(stores):
    if not all(isinstance(store, dict) and 'name' in store and 'age' in store for store in stores):
        raise ValueError("All elements must be dictionaries with 'name' and 'age' keys")
    return [store for store in stores if is_store_eligible(store)]

if __name__ == '__main__':
    filtered_stores = filter_stores(stores)
    print(filtered_stores)