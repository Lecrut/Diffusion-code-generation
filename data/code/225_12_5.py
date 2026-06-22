def find_min_max(d):
    min_val = min((v for v in d.values() if isinstance(v, (int, float))), default=None)
    max_val = max((v for v in d.values() if isinstance(v, (int, float))), default=None)
    min_key = next((k for k, v in d.items() if v == min_val), None)
    max_key = next((k for k, v in d.items() if v == max_val), None)
    return (min_key, min_val), (max_key, max_val)

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2, 'd': 4}
    print(find_min_max(sample_dict))