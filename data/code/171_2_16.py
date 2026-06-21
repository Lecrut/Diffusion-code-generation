import json

def extract_unique_store_names(json_string):
    stores = json.loads(json_string)
    unique_names = set()
    for store in stores:
        name = store.get("name", "Unknown")
        if name:
            unique_names.add(name)
    return sorted(unique_names)

if __name__ == '__main__':
    sample_json = '''
    [
        {
            "name": "Store A",
            "address": "123 Main St",
            "products": ["Laptop", "Mouse", "Keyboard"]
        },
        {
            "name": "Tech Hub Store",
            "address": "456 Elm St, Anytown",
            "products": ["Monitor", "Webcam", "Keyboard"]
        }
    ]
    '''
    store_names = extract_unique_store_names(sample_json)
    print(store_names)