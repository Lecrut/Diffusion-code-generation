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
            "name": "Tech Hub Store",
            "address": "123 Main St, Anytown",
            "products": ["Laptop", "Mouse", "Keyboard"]
        },
        {
            "name": "Book Nook",
            "address": "456 Library Ave, Somewhere",
            "products": ["Novel", "Textbook", "Pen Set"]
        },
        {
            "name": "Grocery Mart",
            "address": "789 Market Rd, Cityville",
            "products": ["Apples", "Bread", "Milk", "Cheese"]
        }
    ]
    json_output = format_store_data_to_json(sample_stores)
    print(json_output)