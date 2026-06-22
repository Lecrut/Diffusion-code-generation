def min_value_from_dict(input_dict, default=None):
    return min(input_dict.values(), default=default)
if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    print(min_value_from_dict(sample_dict))
    print(min_value_from_dict({}, default='Empty'))