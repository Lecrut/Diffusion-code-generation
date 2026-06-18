import json
from datetime import datetime
def generate_item_list():
    items = [
        {"id": 1001, "name": "Laptop", "price": 999.99},
        {"id": 1002, "name": "Mouse", "price": 25.50},
        {"id": 1003, "name": "Keyboard", "price": 75.00}
    ]
    return items
def main():
    item_data = generate_item_list()
    output_format = json.dumps(item_data)
    print(output_format)
if __name__ == '__main__':
    main()