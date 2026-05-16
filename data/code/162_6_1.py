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
    print(safe_map(sample_dict))
    sample_dict_missing = {
        "a": 100,
        "b": 200
    }
    print(safe_map(sample_dict_missing, default=None))
    sample_dict_all_missing = {}
    print(safe_map(sample_dict_all_missing, default=0))