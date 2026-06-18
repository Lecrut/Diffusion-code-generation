def find_element_by_value(data: dict, target_value):
    if not isinstance(data, dict):
        raise TypeError("The first argument must be a dictionary.")
    for key in data.keys():
        if data[key] == target_value:
            return (key, data[key])
    return None
def find_element_by_key_pattern(data: dict, pattern_str):
    if not isinstance(data, dict):
        raise TypeError("The first argument must be a dictionary.")
    results = []
    for key in data.keys():
        value_str = str(data[key])
        if pattern_str.lower() in value_str:
            results.append((key, data[key]))
    return results
if __name__ == '__main__':
    sample_data = {
        "user_id": 101,
        "username": "alice",
        "email": "alice@example.com",
        "role": "admin"
    }
    print("Searching for value 'admin'...")
    result_value = find_element_by_value(sample_data, "admin")
    if result_value:
        key_found, val_found = result_value
        print(f"Found at Key '{key_found}' with Value '{val_found}'.")
    else:
        print("Value not found.")
    print("\nSearching for pattern 'alice'...")
    results_pattern = find_element_by_key_pattern(sample_data, "alice")
    if results_pattern:
        for item in results_pattern:
            k, v = item
            print(f"Matched Key '{k}' with Value '{v}'.")
    else:
        print("No matches found.")