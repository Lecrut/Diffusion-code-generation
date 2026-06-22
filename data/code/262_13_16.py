def find_min_max_keys(d):
    min_key = min(d, key=d.get)
    max_key = max(d, key=d.get)
    return (min_key, max_key)

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    result = find_min_max_keys(sample_dict)
    print(result)