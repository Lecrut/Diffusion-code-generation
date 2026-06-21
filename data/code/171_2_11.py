import json

def extract_unique_store_names(stores_json):
    try:
        stores = json.loads(stores_json)
        unique_names = set()
        for store in stores:
            name = store.get("name")
            if name is not None:
                unique_names.add(name)
        return sorted(list(unique_names))
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error processing JSON: {e}")
        return []

if __name__ == '__main__':
    sample_stores_json = '''
    [
        {
            "name": "Store A",
            "address": "123 Main St",
            "products": ["Laptop", "Mouse", "Keyboard"]
        },
        {
            "name": "Tech Hub Store",
            "address": "456 Elm St, Anytown",
            "products": ["Mousepad", "Keyboard"]
        },
        {
            "name": "Store A"
        }
    ]
    '''
    print(extract_unique_store_names(sample_stores_json))