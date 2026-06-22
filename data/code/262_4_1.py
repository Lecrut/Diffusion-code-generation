def find_min_max(dictionary):
    if not dictionary:
        return None, None
    min_val = max_val = next(iter(dictionary.values()))
    for value in dictionary.values():
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return min_val, max_val

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 4, 'd': 2}
    print(find_min_max(sample_dict))