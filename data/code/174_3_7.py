def validate_dict(d):
    if not isinstance(d, dict):
        raise ValueError("Input must be a dictionary.")
    if len(d) != len(set(d.values())):
        raise ValueError("Dictionary values must be unique.")

def invert_dictionary(d):
    validate_dict(d)
    return {v: k for k, v in d.items()}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    inverted_dict = invert_dictionary(sample_dict)
    print(inverted_dict)