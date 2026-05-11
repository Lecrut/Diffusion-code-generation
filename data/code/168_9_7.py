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
            if item > 10:
                category = "Large Number"
            else:
                category = "Small Number"
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
        15,
        "Banana",
        2,
        "Broccoli",
        30,
        "Orange",
        9,
        42,
        "Grapes"
    ]
    result = group_items(sample_data)
    print(result)