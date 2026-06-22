def get_value_with_fallback(data: dict, key, default=None):
    return data.get(key, default)

if __name__ == '__main__':
    sample_dict = {"a": 1, "b": 2}
    result = get_value_with_fallback(sample_dict, "a", 99)
    print(result)
    result_missing = get_value_with_fallback(sample_dict, "z", 10)
    print(result_missing)