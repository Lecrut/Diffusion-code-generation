import json
def generate_item_list(items):
    if not items:
        raise ValueError("Item list cannot be empty.")
    result = []
    for index, item in enumerate(items, start=1):
        try:
            name = str(item.get('name', 'Unknown'))
            price = float(item.get('price', 0)) if isinstance(item.get('price'), (int, float)) else 0.0
            result.append({
                "index": index,
                "item_name": name,
                "formatted_price": f"${price:.2f}"
            })
        except Exception as e:
            print(f"Warning: Error processing item at index {index}: {e}")
            continue
    return result
if __name__ == '__main__':
    sample_data = [
        {"name": "Laptop", "price": 1200},
        {"name": "Mouse", "price": 25.99},
        {"name": "Keyboard", "price": 75}
    ]
    try:
        item_list = generate_item_list(sample_data)
        print("Generated Item List:")
        for entry in item_list:
            print(f"{entry['index']}. {entry['item_name']} - {entry['formatted_price']}")
        with open('output.json', 'w') as f:
            json.dump(item_list, f)
    except Exception as e:
        print(f"Critical error occurred: {e}")