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
        elif isinstance(item, list):
            category = "List"
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
        "banana",
        [1, 2, 3],
        "grape",
        50,
        "broccoli",
        "orange",
        "a random string"
    ]
    result = group_items(sample_data)
    print(result)