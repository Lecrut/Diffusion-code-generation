def get_value_with_default(data, key, default):
    if key in data:
        return data[key]
    return default

if __name__ == '__main__':
    sample_dict = {"a": 1, "b": 2}
    result = get_value_with_default(sample_dict, "a", 99)
    print(result)
    result2 = get_value_with_default(sample_dict, "c", 100)
    print(result2)