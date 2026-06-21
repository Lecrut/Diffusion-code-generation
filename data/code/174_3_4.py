def invert_dictionary(input_dict):
    return {v: k for k, v in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {'one': 1, 'two': 2, 'three': 3}
    inverted_dict = invert_dictionary(sample_dict)
    print(inverted_dict)