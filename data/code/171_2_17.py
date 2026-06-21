import json

def extract_unique_store_names(stores):
    store_names = set()
    for store in stores:
        name = store.get('name')
        if name is not None:
            store_names.add(name)
    return sorted(store_names)
if __name__ == '__main__':
    sample_stores = [{'name': 'Store A', 'address': '123 Main St', 'products': ['Laptop', 'Mouse', 'Keyboard']}, {'name': 'Tech Hub Store', 'address': '456 Elm St, Anytown', 'products': ['Monitor', 'Speakers', 'USB Cable']}, {'name': 'Store A', 'address': '789 Oak St', 'products': ['Desk', 'Chair', 'File Cabinet']}]
    unique_store_names = extract_unique_store_names(sample_stores)
    print(unique_store_names)