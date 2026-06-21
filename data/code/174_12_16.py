def invert_dict(d):
    return {v: k for k, v in d.items() if isinstance(v, hashable) and len(set(d.values())) == len(d)}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(invert_dict(sample_dict))