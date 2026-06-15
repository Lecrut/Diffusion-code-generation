def safe_get(data, key, default=None):
    return data.get(key, default)
if __name__ == '__main__':
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    print("--- Testing successful retrievals ---")
    value1 = safe_get(sample_data, "apple", 0)
    print(f"Value for 'apple' (default 0): {value1}")
    value2 = safe_get(sample_data, "banana", -1)
    print(f"Value for 'banana' (default -1): {value2}")
    print("\n--- Testing missing key retrieval ---")
    value3 = safe_get(sample_data, "grape", "Not Found")
    print(f"Value for 'grape' (default 'Not Found'): {value3}")
    print("\n--- Testing default behavior with None ---")
    value4 = safe_get(sample_data, "orange")
    print(f"Value for 'orange' (default None): {value4}")