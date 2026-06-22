def min_value(dictionary, default=None):
    return min(dictionary.values(), default=default)
if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    print(min_value(sample_dict))
    empty_dict = {}
    print(min_value(empty_dict, default=0))