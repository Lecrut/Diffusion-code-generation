import json
def generate_item_list(items):
    try:
        return {item['id']: item for item in items} if isinstance(items, list) else {}
    except Exception as e:
        print(f"Error generating item list: {e}")
        return {}
if __name__ == '__main__':
    sample_items = [
        {'id': 101, 'name': 'Laptop', 'price': 999.99},
        {'id': 102, 'name': 'Mouse', 'price': 25.50}
    ]
    item_list = generate_item_list(sample_items)
    output_data = {
        "status": "success",
        "count": len(item_list),
        "items": list(item_list.values())
    }
    with open('item_list.json', 'w') as f:
        json.dump(output_data, f, indent=4)