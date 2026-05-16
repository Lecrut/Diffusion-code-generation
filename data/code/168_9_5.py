def group_items(data):
    grouped = {}
    for item in data:
        category = "Other"
        if isinstance(item, str):
            if item.startswith("A"):
                category = "Category A"
            elif item.startswith("B"):
                category = "Category B"
        elif isinstance(item, int):
            if item > 10:
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
        "Banana",
        "Apricot",
        15,
        2,
        "Ball",
        30,
        "Carrot",
        4,
        99,
        "Ant",
        11
    ]
    result = group_items(sample_data)
    print(result)