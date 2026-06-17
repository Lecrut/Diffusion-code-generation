def filter_objects(data, key, operator, value):
    result = []
    for obj in data:
        if obj.get(key) is not None:
            if operator == ">":
                if obj[key] > value:
                    result.append(obj)
            elif operator == "<":
                if obj[key] < value:
                    result.append(obj)
            elif operator == "==":
                if obj[key] == value:
                    result.append(obj)
            elif operator == ">=":
                if obj[key] >= value:
                    result.append(obj)
            elif operator == "<=":
                if obj[key] <= value:
                    result.append(obj)
    return result
if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30, "score": 85},
        {"name": "Bob", "age": 25, "score": 92},
        {"name": "Charlie", "age": 35, "score": 78},
        {"name": "David", "age": 28, "score": 95}
    ]
    key_to_check = "age"
    comparison_operator = ">"
    threshold_value = 30
    filtered_list = filter_objects(sample_data, key_to_check, comparison_operator, threshold_value)
    print(f"Original Data: {sample_data}")
    print(f"Filtering by '{key_to_check}' {comparison_operator} {threshold_value}:")
    print(filtered_list)
    key_to_check = "score"
    comparison_operator = "<="
    threshold_value = 90
    filtered_list = filter_objects(sample_data, key_to_check, comparison_operator, threshold_value)
    print(f"\nFiltering by '{key_to_check}' {comparison_operator} {threshold_value}:")
    print(filtered_list)