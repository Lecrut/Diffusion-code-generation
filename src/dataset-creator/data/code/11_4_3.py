import json
def detect_uniform_values(data_list):
    try:
        data = [item for item in data_list]
        return len(set(str(item) for item in data)) == 1 and len(data) > 0, set(str(item) for item in data)[0]
    except Exception:
        return False, None
def process_dataset(dataset):
    results = []
    for row_idx, row_data in enumerate(dataset):
        is_uniform, value = detect_uniform_values(row_data)
        if is_uniform and len(value) > 0:
            results.append({"row_index": row_idx, "value": value})
    return results
if __name__ == '__main__':
    sample_dataset = [
        ["1", "2"],
        [],
        ["5", "5"],
        None,
        ["3.0", "3.0"],
        []
    ]
    output = process_dataset(sample_dataset)
    for item in output:
        print(f"Row {item['row_index']}: Uniform value '{item['value']}'")