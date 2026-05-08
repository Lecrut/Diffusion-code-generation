def check_item_in_list(data, key, value):
    for item in data:
        if item.get(key) == value:
            return True
    return False
if __name__ == '__main__':
    sample_list = [
        {"id": 1, "name": "Alice", "city": "New York"},
        {"id": 2, "name": "Bob", "city": "Los Angeles"},
        {"id": 3, "name": "Charlie", "city": "New York"}
    ]
    key_to_check = "city"
    value_to_find = "New York"
    result1 = check_item_in_list(sample_list, key_to_check, value_to_find)
    print(f"Checking for '{value_to_find}' in '{key_to_check}': {result1}")
    key_to_check = "name"
    value_to_find = "Bob"
    result2 = check_item_in_list(sample_list, key_to_check, value_to_find)
    print(f"Checking for '{value_to_find}' in '{key_to_check}': {result2}")
    key_to_check = "country"
    value_to_find = "USA"
    result3 = check_item_in_list(sample_list, key_to_check, value_to_find)
    print(f"Checking for '{value_to_find}' in '{key_to_check}': {result3}")
    key_to_check = "id"
    value_to_find = 3
    result4 = check_item_in_list(sample_list, key_to_check, value_to_find)
    print(f"Checking for {value_to_find} in '{key_to_check}': {result4}")