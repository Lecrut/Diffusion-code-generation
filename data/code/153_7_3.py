def check_item_existence(data, key, value):
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
    result1 = check_item_existence(sample_list, key_to_check, value_to_find)
    print(f"Checking for '{key_to_check}'='{value_to_find}': {result1}")
    key_to_check = "name"
    value_to_find = "Bob"
    result2 = check_item_existence(sample_list, key_to_check, value_to_find)
    print(f"Checking for '{key_to_check}'='{value_to_find}': {result2}")
    key_to_check = "city"
    value_to_find = "London"
    result3 = check_item_existence(sample_list, key_to_check, value_to_find)
    print(f"Checking for '{key_to_check}'='{value_to_find}': {result3}")