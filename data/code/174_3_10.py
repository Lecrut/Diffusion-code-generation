def is_valid_dict(d):
    return isinstance(d, dict) and all(isinstance(v, hashable) for v in d.values())

def invert_dictionary(input_dict):
    if not is_valid_dict(input_dict):
        raise ValueError("Input must be a dictionary with hashable values")
    
    return {v: k for k, v in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {'x': 1, 'y': 2, 'z': 3}
    inverted_dict = invert_dictionary(sample_dict)
    print(inverted_dict)