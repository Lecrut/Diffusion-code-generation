def get_value_with_default(data: dict, key, default=None):
    if key in data:
        return data[key]
    return default

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    result = get_value_with_default(sample_dict, 'a')
    print(result)
    result_missing = get_value_with_default(sample_dict, 'c', 'fallback')
    print(result_missing)