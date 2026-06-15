import json
def format_store_data_to_json(stores):
    output = []
    for store in stores:
        store_data = {
            "name": store.get("name"),
            "address": store.get("address"),
            "products": store.get("products", [])
        }
        output.append(store_data)
    return json.dumps(output, indent=4)
if __name__ == '__main__':
    sample_stores = [
        {
            "name": "Store A",
            "address": "123 Main St",
            "products": ["Laptop", "Mouse", "Keyboard"]
        },
        {
            "name": "Store B",
            "address": "456 Oak Ave",
            "products": ["Monitor", "Webcam"]
        },
        {
            "name": "Store C",
            "address": "789 Pine Ln",
            "products": ["Laptop", "Mouse", "Headset", "Keyboard"]
        }
    ]
    json_output = format_store_data_to_json(sample_stores)
    print(json_output)