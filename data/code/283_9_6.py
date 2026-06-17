def filter_objects(data, key, operator, value):
    result = []
    for obj in data:
        if obj.get(key) is not None:
            if operator == "gt" and obj[key] > value:
                result.append(obj)
            elif operator == "lt" and obj[key] < value:
                result.append(obj)
            elif operator == "eq" and obj[key] == value:
                result.append(obj)
    return result
if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30, "score": 85},
        {"name": "Bob", "age": 25, "score": 92},
        {"name": "Charlie", "age": 35, "score": 78},
        {"name": "David", "age": 28, "score": 95}
    ]
    print("Original Data:")
    for item in sample_data:
        print(item)
    print("\nFiltering by age greater than 30:")
    result_gt = filter_objects(sample_data, "age", "gt", 30)
    for item in result_gt:
        print(item)
    print("\nFiltering by score less than 90:")
    result_lt = filter_objects(sample_data, "score", "lt", 90)
    for item in result_lt:
        print(item)
    print("\nFiltering by age equal to 28:")
    result_eq = filter_objects(sample_data, "age", "eq", 28)
    for item in result_eq:
        print(item)