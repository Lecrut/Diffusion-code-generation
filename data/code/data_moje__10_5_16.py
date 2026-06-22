def get_first_value(d):
    for key in d:
        return d[key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_first_value(sample_dict)
    print(result)