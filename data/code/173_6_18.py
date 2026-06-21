def group_data(data_iterable, key_func):
    groups = {}
    for item in data_iterable:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

if __name__ == '__main__':
    sample_data = [
        "apple,red,fruit",
        "banana,yellow,fruit",
        "carrot,orange,vegetable",
        "grape,purple,fruit",
        "spinach,green,vegetable"
    ]

    key_func = lambda x: x.split(',')[2].strip()
    grouped_data = group_data(sample_data, key_func)
    for key, items in grouped_data.items():
        print(f"{key}: {items}")