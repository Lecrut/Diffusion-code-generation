def invert_dict(d):
    return {v: k for k, v in d.items()}

if __name__ == '__main__':
    sample_dict = {'one': 1, 'two': 2, 'three': 3}
    inverted_dict = invert_dict(sample_dict)
    print(inverted_dict)