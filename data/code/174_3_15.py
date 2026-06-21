def invert_dict(d):
    if not isinstance(d, dict) or not all(isinstance(v, hashable) and v is not None for v in d.values()):
        raise ValueError("Input must be a dictionary with hashable, non-None values.")
    return {v: k for k, v in d.items()}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    inverted_dict = invert_dict(sample_dict)
    print(inverted_dict)