def invert_dict(d):
    if not all(isinstance(v, hashable) and isinstance(k, hashable) for k, v in d.items()):
        raise ValueError("All keys and values must be hashable")
    
    return {v: k for k, v in d.items()}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    inverted_dict = invert_dict(sample_dict)
    print(inverted_dict)