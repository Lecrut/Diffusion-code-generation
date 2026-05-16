def safe_map(data, default=None):
    result = {}
    for key in data:
        result[key] = data.get(key, default)
    return result
if __name__ == '__main__':
    sample_dict = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    sample_dict_missing = {
        "a": 100,
        "b": 200
    }
    mapped_values_1 = safe_map(sample_dict)
    print(f"Sample 1 Result: {mapped_values_1}")
    mapped_values_2 = safe_map(sample_dict_missing, default=None)
    print(f"Sample 2 Result (with default=None): {mapped_values_2}")
    mapped_values_3 = safe_map(sample_dict_missing, default="Not Found")
    print(f"Sample 3 Result (with default=\"Not Found\"): {mapped_values_3}")