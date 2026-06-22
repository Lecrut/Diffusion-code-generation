def max_min_diff(dictionary):
    return max(dictionary.values()) - min(dictionary.values())

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 5, 'c': 1}
    print(max_min_diff(sample_dict))