import json

def extract_unique_store_names(stores):
    store_names = set()
    for store in stores:
        if "name" in store:
            store_names.add(store["name"])
    return sorted(list(store_names))

if __name__ == '__main__':
    sample_stores = [
        {
            "name": "Store A",
            "address": "123 Main St",
            "products": ["Laptop", "Mouse", "Keyboard"]
        },
        {
            "name": "Tech Hub Store",
            "address": "456 Elm St, Anytown",
            "products": ["Monitor", "USB Cable", "Headphones"]
        },
        {
            "name": "Store A",
            "address": "789 Oak St",
            "products": ["Laptop Bag", "Mouse Pad"]
        }
    ]
    unique_store_names = extract_unique_store_names(sample_stores)
    print(unique_store_names)