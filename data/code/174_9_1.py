def safe_get(data, key, default=None):
    return data.get(key, default)
if __name__ == '__main__':
    sample_dict = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    print("--- Test Case 1: Key exists ---")
    value1 = safe_get(sample_dict, "apple", 0)
    print(f"Value for 'apple' (default 0): {value1}")
    print("\n--- Test Case 2: Key missing, using default ---")
    value2 = safe_get(sample_dict, "grape", "Not Found")
    print(f"Value for 'grape' (default 'Not Found'): {value2}")
    print("\n--- Test Case 3: Key missing, using None default ---")
    value3 = safe_get(sample_dict, "orange")
    print(f"Value for 'orange' (default None): {value3}")
    print("\n--- Test Case 4: Retrieving an existing key with a specific default ---")
    value4 = safe_get(sample_dict, "banana", -1)
    print(f"Value for 'banana' (default -1): {value4}")