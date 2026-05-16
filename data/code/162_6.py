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
    result1 = safe_map(sample_dict, None)
    print(result1)
    result2 = safe_map(sample_dict, 0)
    print(result2)
    empty_dict = {}
    result3 = safe_map(empty_dict, "Not Found")
    print(result3)
    mixed_dict = {
        "a": 100,
        "b": 200
    }
    result4 = safe_map(mixed_dict, 999)
    print(result4)