def get_first_value(d):
    return next(iter(d.values()))

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_first_value(sample_dict)
    print(result)