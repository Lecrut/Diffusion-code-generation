def filter_dict(input_dict):
    return [(key, value) for key, value in input_dict.items() if value >= 0]

if __name__ == '__main__':
    sample_dict = {'a': -1, 'b': 2, 'c': 3, 'd': -4}
    result = filter_dict(sample_dict)
    print(result)