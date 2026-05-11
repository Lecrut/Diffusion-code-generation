def safe_map(data, default_value):
    result = {}
    for key in data:
        result[key] = data.get(key, default_value)
    return result
if __name__ == '__main__':
    sample_dict = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    sample_dict_missing = {
        "a": 10,
        "b": 20
    }
    sample_dict_mixed = {
        "x": 100,
        "y": None,
        "z": 300
    }
    default = None
    result1 = safe_map(sample_dict, default)
    print(f"Result 1: {result1}")
    result2 = safe_map(sample_dict_missing, default)
    print(f"Result 2: {result2}")
    result3 = safe_map(sample_dict_mixed, default)
    print(f"Result 3: {result3}")