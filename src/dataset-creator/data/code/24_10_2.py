import json
def generate_item_list():
    items = [
        {"id": 1001, "name": "Laptop", "category": "Electronics"},
        {"id": 1002, "name": "Desk Chair", "category": "Furniture"},
        {"id": 1003, "name": "Wireless Mouse", "category": "Accessories"}
    ]
    try:
        with open("items.json", "w") as f:
            json.dump(items, f, indent=4)
        return items
    except IOError as e:
        print(f"Error writing file: {e}")
        raise
if __name__ == '__main__':
    try:
        item_list = generate_item_list()
        for item in item_list:
            print(json.dumps(item))
    except Exception as ex:
        print(f"Unexpected error occurred: {ex}")