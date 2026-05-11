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
        "a": 10,
        "b": 20
    }
    result1 = safe_map(sample_dict, None)
    print(f"Result 1: {result1}")
    result2 = safe_map(sample_dict_missing, 99)
    print(f"Result 2: {result2}")