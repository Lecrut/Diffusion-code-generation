def filter_objects(data, key, operator, value):
    result = []
    for obj in data:
        if operator == "gt" and obj.get(key, float('-inf')) > value:
            result.append(obj)
        elif operator == "lt" and obj.get(key, float('inf')) < value:
            result.append(obj)
        elif operator == "ge" and obj.get(key, float('-inf')) >= value:
            result.append(obj)
        elif operator == "le" and obj.get(key, float('inf')) <= value:
            result.append(obj)
    return result
if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "score": 85, "age": 30},
        {"name": "Bob", "score": 92, "age": 25},
        {"name": "Charlie", "score": 78, "age": 35},
        {"name": "David", "score": 95, "age": 28}
    ]
    key_to_check = "score"
    comparison_operator = "gt"
    threshold_value = 90
    filtered_list = filter_objects(sample_data, key_to_check, comparison_operator, threshold_value)
    print(f"Original Data: {sample_data}")
    print(f"Filtering by '{key_to_check}' {comparison_operator} {threshold_value}:")
    print(filtered_list)
    key_to_check = "age"
    comparison_operator = "le"
    threshold_value = 30
    filtered_list = filter_objects(sample_data, key_to_check, comparison_operator, threshold_value)
    print(f"\nFiltering by '{key_to_check}' {comparison_operator} {threshold_value}:")
    print(filtered_list)