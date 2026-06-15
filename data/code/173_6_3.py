def group_data(data, group_index):
    grouped = {}
    for line in data:
        if not line.strip():
            continue
        key = line[group_index].strip()
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(line)
    return grouped
if __name__ == '__main__':
    sample_data = [
        "apple,red,fruit",
        "banana,yellow,fruit",
        "carrot,orange,vegetable",
        "grape,purple,fruit",
        "spinach,green,vegetable"
    ]
    group_column_index = 1
    result = group_data(sample_data, group_column_index)
    print(result)