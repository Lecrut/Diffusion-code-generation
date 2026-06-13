def safe_get(data, key, default=None):
    return data.get(key, default)
if __name__ == '__main__':
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    print("--- Test Case 1: Key exists ---")
    value1 = safe_get(sample_data, "apple", 0)
    print(f"Value for 'apple' (default 0): {value1}")
    print("\n--- Test Case 2: Key missing, using default None ---")
    value2 = safe_get(sample_data, "grape")
    print(f"Value for 'grape' (default None): {value2}")
    print("\n--- Test Case 3: Key missing, using custom default value ---")
    value3 = safe_get(sample_data, "orange", -1)
    print(f"Value for 'orange' (default -1): {value3}")
    print("\n--- Test Case 4: Empty dictionary test ---")
    empty_data = {}
    value4 = safe_get(empty_data, "test_key", "MISSING")
    print(f"Value for 'test_key' in empty dict (default 'MISSING'): {value4}")