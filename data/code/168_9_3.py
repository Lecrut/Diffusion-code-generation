def group_items(data):
    grouped = {}
    for item in data:
        category = "Other"
        if isinstance(item, str):
            if item.startswith("A"):
                category = "A_Items"
            elif item.startswith("B"):
                category = "B_Items"
            else:
                category = "C_Items"
        elif isinstance(item, int):
            if item > 10:
                category = "Large_Numbers"
            else:
                category = "Small_Numbers"
        else:
            category = "Miscellaneous"
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item)
    return grouped
if __name__ == '__main__':
    sample_data = [
        "Apple",
        "Banana",
        "Apricot",
        "Carrot",
        "Ball",
        15,
        2,
        30,
        "Avocado",
        4,
        "Berry"
    ]
    result = group_items(sample_data)
    print(result)