import json

class StoreParser:
    STORE_NAME_KEY = "name"
    
    @staticmethod
    def extract_unique_store_names(stores):
        store_names = set()
        for store in stores:
            name = store.get(StoreParser.STORE_NAME_KEY, None)
            if name is not None:
                store_names.add(name)
        return sorted(store_names)

if __name__ == '__main__':
    sample_stores = [
        {
            "name": "Tech Hub Store",
            "address": "123 Main St, Anytown",
            "products": ["Laptop", "Mouse", "Keyboard"]
        },
        {
            "name": "Store A",
            "address": "456 Elm St",
            "products": ["Monitor", "Headphones"]
        },
        {
            "name": "Tech Hub Store"
        }
    ]
    
    parser = StoreParser()
    unique_store_names = parser.extract_unique_store_names(sample_stores)
    print(unique_store_names)