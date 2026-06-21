def get_dict_value(d, key, default=None):
    if key in d:
        return d[key]
    return default

if __name__ == '__main__':
    sample_dict = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
    print(get_dict_value(sample_dict, 'name'))
    print(get_dict_value(sample_dict, 'country', 'Unknown'))
    print(get_dict_value(sample_dict, 'age'))
    print(get_dict_value({}, 'any_key', 'Fallback'))