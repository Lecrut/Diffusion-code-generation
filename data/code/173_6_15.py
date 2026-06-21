def group_data(data_iterable, key_func):
    def _group_next_item(groups, item):
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
        return groups

    grouped = {}
    for item in data_iterable:
        if item.strip():
            grouped = _group_next_item(grouped, item.split(','))
    return grouped

if __name__ == '__main__':
    sample_data = [
        "apple,red,fruit",
        "banana,yellow,fruit",
        "carrot,orange,vegetable",
        "grape,purple,fruit",
        "spinach,green,vegetable"
    ]
    result = group_data(sample_data, lambda x: x[2])
    print(result)