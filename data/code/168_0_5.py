def categorize_items(items):
    categories = {
        "fruits": [],
        "vegetables": [],
        "meats": [],
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
            elif "beef" in lower_item or "chicken" in lower_item or "pork" in lower_item:
                categories["meats"].append(item)
            elif "milk" in lower_item or "cheese" in lower_item or "yogurt" in lower_item:
                categories["dairy"].append(item)
            else:
                categories["other"].append(item)
        else:
            categories["other"].append(item)
    return categories
if __name__ == '__main__':
    sample_data = [
        "Apple",
        "Carrot",
        "Beef",
        "Milk",
        "Banana",
        "Broccoli",
        "Cheese",
        "Steak",
        "Water",
        123,
        "Orange"
    ]
    grouped_items = categorize_items(sample_data)
    for category, items in grouped_items.items():
        print(f"--- {category.capitalize()} ---")
        for item in items:
            print(item)
        print()