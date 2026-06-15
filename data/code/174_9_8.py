def safe_get(data_dict, key, default_value):
    return data_dict.get(key, default_value)
if __name__ == '__main__':
    sample_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    print("--- Testing successful retrievals ---")
    print("Value for 'apple':", safe_get(sample_data, "apple", "Not Found"))
    print("Value for 'banana':", safe_get(sample_data, "banana", "Not Found"))
    print("\n--- Testing missing key retrieval (using default) ---")
    print("Value for 'grape' (defaulting to 'Missing'):", safe_get(sample_data, "grape", "Missing"))
    print("Value for 'orange' (defaulting to 0):", safe_get(sample_data, "orange", 0))
    print("\n--- Testing retrieval with different defaults ---")
    print("Value for 'cherry' (defaulting to -1):", safe_get(sample_data, "cherry", -1))