import json
def format_store_data_to_json(stores):
    output_data = []
    for store in stores:
        formatted_store = {
            "name": store.get("name", "N/A"),
            "address": store.get("address", "N/A"),
            "products": store.get("products", [])
        }
        output_data.append(formatted_store)
    return json.dumps(output_data, indent=4)
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
            "products": ["Laptop", "Mouse", "Headset", "Webcam"]
        }
    ]
    json_output = format_store_data_to_json(sample_stores)
    print(json_output)