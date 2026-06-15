def safe_get(data_dict, key, default_value):
    return data_dict.get(key, default_value)
if __name__ == '__main__':
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    print("--- Test Case 1: Key exists ---")
    value1 = safe_get(sample_data, "apple", 0)
    print(f"Retrieved value for 'apple': {value1}")
    print("\n--- Test Case 2: Key does not exist (using default) ---")
    value2 = safe_get(sample_data, "grape", "Not Found")
    print(f"Retrieved value for 'grape': {value2}")
    print("\n--- Test Case 3: Another missing key ---")
    value3 = safe_get(sample_data, "orange", -1)
    print(f"Retrieved value for 'orange': {value3}")