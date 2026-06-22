def min_value_from_dict(input_dict, default=None):
    if not input_dict:
        return default
    return min(input_dict.values())
if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    print(min_value_from_dict(sample_dict))
    empty_dict = {}
    print(min_value_from_dict(empty_dict, default=0))