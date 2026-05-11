def categorize_items(items):
    categories = {
        "fruits": [],
        "vegetables": [],
        "dairy": [],
        "other": []
    }
    for item in items:
        if isinstance(item, str):
            lower_item = item.lower()
            if "apple" in lower_item or "banana" in lower_item or "orange" in lower_item:
                categories["fruits"].append(item)
            elif "carrot" in lower_item or "broccoli" in lower_item or "spinach" in lower_item:
                categories["vegetables"].append(item)
            elif "milk" in lower_item or "cheese" in lower_item:
                categories["dairy"].append(item)
            else:
                categories["other"].append(item)
        elif isinstance(item, dict):
            if item.get("type") == "fruit":
                categories["fruits"].append(item.get("name"))
            elif item.get("type") == "vegetable":
                categories["vegetables"].append(item.get("name"))
            elif item.get("type") == "dairy":
                categories["dairy"].append(item.get("name"))
            else:
                categories["other"].append(item.get("name"))
    return categories
if __name__ == '__main__':
    sample_data = [
        "Apple",
        "Carrot",
        "Milk",
        "Banana",
        {"name": "Grape", "type": "fruit"},
        "Broccoli",
        "Cheese",
        "Steak",
        "Orange"
    ]
    result = categorize_items(sample_data)
    print(result)