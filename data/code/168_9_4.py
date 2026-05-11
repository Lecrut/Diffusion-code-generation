def group_items(data):
    grouped = {}
    for item in data:
        category = "Other"
        if isinstance(item, str):
            if "fruit" in item.lower():
                category = "Fruit"
            elif "vegetable" in item.lower():
                category = "Vegetable"
            else:
                category = "String"
        elif isinstance(item, int):
            category = "Number"
        elif isinstance(item, float):
            category = "Number"
        else:
            category = "Unknown"
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item)
    return grouped
if __name__ == '__main__':
    sample_data = [
        "apple",
        10,
        "carrot",
        3.14,
        "banana",
        50,
        "grape",
        1.0,
        "spinach",
        99
    ]
    result = group_items(sample_data)
    print(result)