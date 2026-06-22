def get_value(data, key, default=None):
    if key in data:
        return data[key]
    return default

if __name__ == '__main__':
    sample_dict = {"a": 1, "b": 2}
    print(get_value(sample_dict, "a"))
    print(get_value(sample_dict, "c", "missing"))
    sample_class = None
    print(get_value({}, "any_key", 42))