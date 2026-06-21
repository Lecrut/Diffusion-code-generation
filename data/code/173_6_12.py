def group_data(data, key_func):
    groups = {}
    for item in data:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

def group_by_category(category):
    return lambda item: item[category]

if __name__ == '__main__':
    sample_data = [
        ["apple", "red", "fruit"],
        ["banana", "yellow", "fruit"],
        ["carrot", "orange", "vegetable"],
        ["grape", "purple", "fruit"],
        ["spinach", "green", "vegetable"]
    ]
    
    grouped_by_color = group_data(sample_data, lambda item: item[1])
    print("Grouped by color:", grouped_by_color)
    
    grouped_by_type = group_data(sample_data, group_by_category(2))
    print("Grouped by type:", grouped_by_type)