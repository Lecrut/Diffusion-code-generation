def invert_dict(d):
    return {v: k for k, v in d.items() if isinstance(v, hashable) and len(set([v])) == 1}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    inverted_dict = invert_dict(sample_dict)
    print(inverted_dict)