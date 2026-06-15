import json
def format_store_data_to_json(stores):
    output = []
    for store in stores:
        store_info = {
            "name": store.get("name"),
            "address": store.get("address"),
            "products": store.get("products", [])
        }
        output.append(store_info)
    return json.dumps(output, indent=4)
if __name__ == '__main__':
    sample_stores = [
        {
            "name": "Tech Hub Store",
            "address": "123 Main St, Anytown",
            "products": ["Laptop", "Mouse", "Keyboard"]
        },
        {
            "name": "Book Nook",
            "address": "456 Oak Ave, Somewhere",
            "products": ["Novel", "Textbook", "Pen Set", "Notebook"]
        },
        {
            "name": "Art Supply Co.",
            "address": "789 Pine Ln, Otherville",
            "products": ["Pencil", "Eraser", "Paint Set"]
        }
    ]
    json_output = format_store_data_to_json(sample_stores)
    print(json_output)