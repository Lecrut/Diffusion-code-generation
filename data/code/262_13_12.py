def find_extreme_keys(d):
    if not d:
        return None, None
    min_key = max_key = list(d.keys())[0]
    for key in d:
        if d[key] < d[min_key]:
            min_key = key
        elif d[key] > d[max_key]:
            max_key = key
    return min_key, max_key

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2, 'd': 4}
    print(find_extreme_keys(sample_dict))