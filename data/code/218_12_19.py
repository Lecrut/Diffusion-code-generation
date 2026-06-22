def find_smallest(input_dict, default=None):
    if not input_dict:
        return default
    try:
        return min(input_dict.values())
    except ValueError:
        return default

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 5, 'c': -3, 'd': 8, 'e': 2}
    result = find_smallest(sample_dict)
    print(result)