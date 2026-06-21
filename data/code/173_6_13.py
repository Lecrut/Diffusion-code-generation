def group_data(data, key_func):
    if not callable(key_func):
        raise ValueError("key_func must be a callable")
    
    groups = {}
    for item in data:
        try:
            key = key_func(item)
            if key not in groups:
                groups[key] = []
            groups[key].append(item)
        except Exception as e:
            print(f"Error processing item: {item}. Error: {e}")
    return groups

def group_by_category(item):
    return item.split(",")[2]

if __name__ == '__main__':
    sample_data = [
        "apple,red,fruit",
        "banana,yellow,fruit",
        "carrot,orange,vegetable",
        "grape,purple,fruit",
        "spinach,green,vegetable"
    ]
    grouped_data = group_data(sample_data, key_func=group_by_category)
    for category, items in grouped_data.items():
        print(f"{category}: {items}")