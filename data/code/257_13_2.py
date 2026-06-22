def calculate_diff(dictionary):
    if not dictionary:
        return 0
    return max(dictionary.values()) - min(dictionary.values())

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 5}
    print(calculate_diff(sample_dict))