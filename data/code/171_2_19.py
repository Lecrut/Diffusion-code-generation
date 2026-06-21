import json

def extract_unique_store_names(stores):
    store_names = set()
    for store in stores:
        name = store.get("name")
        if name:
            store_names.add(name)
    return sorted(store_names)

if __name__ == '__main__':
    sample_stores = [
        {
            "name": "Store A",
            "address": "123 Main St",
            "products": ["Laptop", "Mouse", "Keyboard"]
        },
        {
            "name": "Store B",
            "address": "456 Elm St",
            "products": ["Monitor", "Webcam", "USB Cable"]
        },
        {
            "name": "Store A",
            "address": "789 Oak St",
            "products": ["Keyboard", "Mouse Pad", "Headphones"]
        }
    ]
    unique_store_names = extract_unique_store_names(sample_stores)
    print(unique_store_names)