def group_data(data, index):
    groups = {}
    for line in data:
        if not line.strip():
            continue
        key = line[index].strip()
        if key not in groups:
            groups[key] = []
        groups[key].append(line)
    return groups
if __name__ == '__main__':
    sample_data = [
        "apple,red,fruit",
        "banana,yellow,fruit",
        "carrot,orange,vegetable",
        "grape,purple,fruit",
        "spinach,green,vegetable"
    ]
    column_index = 1
    grouped_result = group_data(sample_data, column_index)
    print(grouped_result)