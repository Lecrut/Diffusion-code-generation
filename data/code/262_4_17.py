def find_min_max(d):
    if not d:
        return None, None
    min_val = max_val = next(iter(d.values()))
    for val in d.values():
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
    return min_val, max_val

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 3}
    print(find_min_max(sample_dict))