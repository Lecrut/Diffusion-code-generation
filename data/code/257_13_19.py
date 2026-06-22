def calculate_range(dictionary):
    if not dictionary:
        return 0
    return max(dictionary.values()) - min(dictionary.values())

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 5, 'c': 1}
    print(calculate_range(sample_dict))