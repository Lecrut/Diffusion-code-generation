def filter_list_by_key_and_operator(data_list, key, operator, value):
    result_list = []
    for item in data_list:
        if key in item:
            item_value = item[key]
            if operator == "greater_than" and isinstance(item_value, (int, float)) and isinstance(value, (int, float)):
                if item_value > value:
                    result_list.append(item)
            elif operator == "less_than" and isinstance(item_value, (int, float)) and isinstance(value, (int, float)):
                if item_value < value:
                    result_list.append(item)
            elif operator == "greater_than_or_equal" and isinstance(item_value, (int, float)) and isinstance(value, (int, float)):
                if item_value >= value:
                    result_list.append(item)
            elif operator == "less_than_or_equal" and isinstance(item_value, (int, float)) and isinstance(value, (int, float)):
                if item_value <= value:
                    result_list.append(item)
    return result_list
if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30, "score": 85.5},
        {"name": "Bob", "age": 25, "score": 92.1},
        {"name": "Charlie", "age": 35, "score": 78.9},
        {"name": "David", "age": 28, "score": 95.0},
        {"name": "Eve", "age": 40, "score": 81.2}
    ]
    print("Original Data:")
    for item in sample_data:
        print(item)
    print("\nFiltering for age greater than 30:")
    result1 = filter_list_by_key_and_operator(sample_data, "age", "greater_than", 30)
    for item in result1:
        print(item)
    print("\nFiltering for score less than 90.0:")
    result2 = filter_list_by_key_and_operator(sample_data, "score", "less_than", 90.0)
    for item in result2:
        print(item)
    print("\nFiltering for age greater than or equal to 35:")
    result3 = filter_list_by_key_and_operator(sample_data, "age", "greater_than_or_equal", 35)
    for item in result3:
        print(item)