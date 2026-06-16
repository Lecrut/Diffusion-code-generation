import json
def generate_item_list():
    raw_data = [
        {"id": 101, "name": "Widget A", "price": 29.99},
        {"id": 102, "name": "Gadget B", "price": -5.00},
        {"id": None, "name": "", "price": "invalid"},
    ]
    validated_items = []
    for item in raw_data:
        try:
            if not isinstance(item.get("id"), int) or item["id"] <= 0:
                continue
            name = str(item.get("name", "")).strip()
            price_str = str(item.get("price"))
            float_price = float(price_str)
            if float_price < 0:
                continue
            validated_items.append({
                "id": item["id"],
                "name": name,
                "price": round(float_price, 2)
            })
        except (ValueError, TypeError):
            continue
    return validated_items
if __name__ == '__main__':
    items = generate_item_list()
    output_json = json.dumps(items, indent=4)
    print(output_json)