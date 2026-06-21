def get_value(d, key, default=None):
    return d.get(key, default)

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result1 = get_value(sample_dict, 'b')
    result2 = get_value(sample_dict, 'd', 0)
    print(result1)
    print(result2)