def safe_get(data, key, default=None):
    return data.get(key, default)
if __name__ == '__main__':
    sample_dict = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    print("--- Testing successful retrievals ---")
    value1 = safe_get(sample_dict, "apple", 0)
    print(f"Value for 'apple' (default 0): {value1}")
    value2 = safe_get(sample_dict, "banana", -1)
    print(f"Value for 'banana' (default -1): {value2}")
    print("\n--- Testing missing key retrieval ---")
    value3 = safe_get(sample_dict, "grape", "Not Found")
    print(f"Value for 'grape' (default 'Not Found'): {value3}")
    value4 = safe_get(sample_dict, "orange", 99)
    print(f"Value for 'orange' (default 99): {value4}")