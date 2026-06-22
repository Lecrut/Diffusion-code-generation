def get_dict_value(d, key, default=None):
    return d.get(key, default)

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(get_dict_value(sample_dict, 'a'))
    print(get_dict_value(sample_dict, 'z', 'default_value'))