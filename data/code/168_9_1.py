def group_items(data):
    grouped = {}
    for item in data:
        category = "Other"
        if isinstance(item, str):
            if "fruit" in item.lower():
                category = "Fruit"
            elif "vegetable" in item.lower():
                category = "Vegetable"
        elif isinstance(item, int):
            if item > 100:
                category = "Large Numbers"
            else:
                category = "Small Numbers"
        else:
            category = "Miscellaneous"
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item)
    return grouped
if __name__ == '__main__':
    sample_data = [
        "Apple",
        "Carrot",
        150,
        "Banana",
        200,
        "Broccoli",
        50,
        "Orange",
        300,
        "Grapes",
        99,
        "Potato"
    ]
    result = group_items(sample_data)
    print(result)