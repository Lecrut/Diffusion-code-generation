def group_data(data, column_index):
    grouped = {}
    for line in data:
        if not line.strip():
            continue
        key = line[column_index].strip()
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(line)
    return grouped
if __name__ == '__main__':
    sample_data = [
        "Apple,Red,Fruit",
        "Banana,Yellow,Fruit",
        "Carrot,Orange,Vegetable",
        "Broccoli,Green,Vegetable",
        "Apple,Red,Fruit",
        "Carrot,Orange,Vegetable"
    ]
    column_to_group = 1
    result = group_data(sample_data, column_to_group)
    print(result)