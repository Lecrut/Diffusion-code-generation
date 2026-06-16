import json
def filter_groups(data):
    filtered = []
    for group in data:
        numeric_values = [float(x) for x in group if isinstance(x, (int, float))]
        if len(numeric_values) > 0 and all(v == numeric_values[0] for v in numeric_values):
            filtered.append(group)
    return filtered
if __name__ == '__main__':
    sample_data = [
        ["A", "1.5"],
        ["B", "2.0", "3.0"],
        ["C", "4.0", "4.0"]
    ]
    result = filter_groups(sample_data)
    print(json.dumps(result, indent=2))