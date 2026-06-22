def find_extreme_keys(d):
    if not d:
        return None, None
    min_key = max_key = list(d.keys())[0]
    for k, v in d.items():
        if v < d[min_key]:
            min_key = k
        elif v > d[max_key]:
            max_key = k
    return min_key, max_key

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
    print(find_extreme_keys(sample_dict))