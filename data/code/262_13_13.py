def find_extreme_keys(d):
    min_key = max_key = None
    min_value = float('inf')
    max_value = float('-inf')

    for key, value in d.items():
        if value < min_value:
            min_value = value
            min_key = key
        elif value > max_value:
            max_value = value
            max_key = key

    return min_key, max_key

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    print(find_extreme_keys(sample_dict))