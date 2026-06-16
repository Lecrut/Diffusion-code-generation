import json
def build_item_list(data):
    items = []
    for key in sorted(data.keys()):
        value = data[key]
        if isinstance(value, dict):
            nested_items = {k: v for k, v in value.items() if not (isinstance(v, str) and 'hidden' in v.lower())}
            items.append({key: nested_items})
    return {"items": items}
if __name__ == '__main__':
    sample_data = {
        "electronics": {
            "phone": "iPhone 15 Pro",
            "laptop": "MacBook Air M2"
        },
        "clothing": {
            "shirt": "Cotton T-Shirt (hidden: size details)",
            "pants": "Denim Jeans"
        }
    }
    result = build_item_list(sample_data)
    print(json.dumps(result, indent=4))