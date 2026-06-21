def invert_dict(input_dict):
    return {v: k for k, v in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    inverted_dict = invert_dict(sample_dict)
    print(inverted_dict)