import json
def detect_uniform_values(data):
    if not isinstance(data, list) or len(data) == 0:
        return False
    first_value = data[0]
    for item in data:
        try:
            comparable_item = float(item)
            if comparable_item != first_value:
                return False
        except (ValueError, TypeError):
            return False
    return True
def process_dataset(dataset_name="sample_data"):
    datasets = {
        "uniform_int": [5, 5, 5],
        "mixed_values": [10, 20, 30],
        "empty_list": [],
        "string_uniform": ["a", "a", "a"],
        "float_uniform": [3.14, 3.14, 3.14],
        "invalid_mixed": [5, "five", 5]
    }
    if dataset_name not in datasets:
        raise ValueError(f"Unknown dataset name: {dataset_name}")
    data = datasets[dataset_name]
    result = detect_uniform_values(data)
    return {"name": dataset_name, "data": data, "is_uniform": result}
if __name__ == '__main__':
    test_cases = ["uniform_int", "mixed_values", "empty_list", "string_uniform"]
    for case in test_cases:
        try:
            outcome = process_dataset(case)
            print(f"Dataset '{outcome['name']}': Uniform values detected? {outcome['is_uniform']}")
        except Exception as e:
            print(f"Error processing dataset '{case}': {e}")