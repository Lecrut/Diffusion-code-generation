import json
from datetime import datetime
def generate_item_list():
    items = [
        {"id": 1001, "name": "Laptop", "price": 999.99},
        {"id": 1002, "name": "Mouse", "price": 25.50},
        {"id": 1003, "name": "Keyboard", "price": 75.00},
    ]
    return items
def main():
    item_list = generate_item_list()
    output_data = {
        "generated_at": datetime.now().isoformat(),
        "total_items": len(item_list),
        "items": item_list,
    }
    print(json.dumps(output_data, indent=2))
if __name__ == '__main__':
    main()