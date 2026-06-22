def get_value_or_default(data, key, default):
    try:
        return data[key]
    except KeyError:
        return default

if __name__ == '__main__':
    sample_dict = {'x': 10, 'y': 20}
    result_found = get_value_or_default(sample_dict, 'x', 0)
    result_missing = get_value_or_default(sample_dict, 'z', 999)
    print(result_found)
    print(result_missing)