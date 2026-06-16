import json
def filter_consistent_groups(data):
    filtered = []
    for group in data:
        if 'numeric_values' not in group:
            continue
        values = [float(v) for v in group['numeric_values']]
        is_consistent = all(abs(values[i] - values[0]) < 1e-9 
                          for i in range(1, len(values)))
        if is_consistent:
            filtered.append(group)
    return filtered
if __name__ == '__main__':
    sample_data = [
        {
            "id": 101,
            "group_name": "Alpha",
            "numeric_values": ["5.0", "5.0", "5.0"]
        },
        {
            "id": 102,
            "group_name": "Beta",
            "numeric_values": ["3.0", "4.0", "5.0"]
        },
        {
            "id": 103,
            "group_name": "Gamma",
            "numeric_values": ["7.2", "7.20", "7.2"]
        }
    ]
    result = filter_consistent_groups(sample_data)
    output_json = json.dumps(result, indent=4)
    print(output_json)