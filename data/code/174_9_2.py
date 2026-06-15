def safe_get(data, key, default=None):
    return data.get(key, default)
if __name__ == '__main__':
    sample_dict = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    print("--- Testing successful retrievals ---")
    print("Value for 'apple':", safe_get(sample_dict, "apple", "Not Found"))
    print("Value for 'banana':", safe_get(sample_dict, "banana", "Not Found"))
    print("\n--- Testing missing key retrieval with default value ---")
    print("Value for 'grape' (default None):", safe_get(sample_dict, "grape"))
    print("Value for 'grape' (default 'MISSING'):", safe_get(sample_dict, "grape", "MISSING"))
    print("\n--- Testing retrieval of a non-existent key with custom default ---")
    print("Value for 'orange' (default 0):", safe_get(sample_dict, "orange", 0))