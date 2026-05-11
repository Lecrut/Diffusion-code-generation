def group_items(data):
    grouped = {}
    for item in data:
        category = "Other"
        if isinstance(item, str):
            if item.startswith("A"):
                category = "A_Items"
            elif item.startswith("B"):
                category = "B_Items"
        elif isinstance(item, int):
            if item > 10:
                category = "Large_Numbers"
            else:
                category = "Small_Numbers"
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item)
    return grouped
if __name__ == '__main__':
    sample_data = [
        "Apple",
        "Banana",
        "Apricot",
        15,
        2,
        "Ball",
        30,
        "Carrot",
        5,
        "Ant"
    ]
    result = group_items(sample_data)
    print(result)