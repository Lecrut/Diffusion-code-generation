def find_min_max(d):
    min_val = min((v for v in d.values()))
    max_val = max((v for v in d.values()))
    min_key = next(k for k, v in d.items() if v == min_val)
    max_key = next(k for k, v in d.items() if v == max_val)
    return (min_key, min_val), (max_key, max_val)

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 4, 'd': 2}
    print(find_min_max(sample_dict))