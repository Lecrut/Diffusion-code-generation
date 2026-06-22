def min_dict_value(d, default=None):
    return min(d.values(), default=default)
if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    print(min_dict_value(sample_dict))
    empty_dict = {}
    print(min_dict_value(empty_dict, default='No values'))