import json
def format_stores_to_json(store_list):
    output = []
    for store in store_list:
        formatted_store = {
            "name": store.get("name", "N/A"),
            "address": store.get("address", "N/A"),
            "products": store.get("products", [])
        }
        output.append(formatted_store)
    return json.dumps(output, indent=4)
if __name__ == '__main__':
    sample_data = [
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
    json_output = format_stores_to_json(sample_data)
    print(json_output)