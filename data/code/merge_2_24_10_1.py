import json
def generate_item_list():
    items = [
        {"id": 1001, "name": "Laptop", "price": 999.99},
        {"id": 1002, "name": "Mouse", "price": 25.50},
        {"id": 1003, "name": "Keyboard", "price": 75.00}
    ]
    try:
        with open("item_list.json", "w") as file:
            json.dump(items, file, indent=4)
        return True
    except IOError as e:
        print(f"Error writing to file: {e}")
        return False
if __name__ == '__main__':
    success = generate_item_list()
    if not success:
        exit(1)