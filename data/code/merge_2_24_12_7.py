import json
def build_item_list(items_data):
    return items_data
if __name__ == '__main__':
    sample_items = [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Mouse", "price": 25.50},
        {"id": 3, "name": "Keyboard", "price": 75.00}
    ]
    result = build_item_list(sample_items)
    print(json.dumps(result))