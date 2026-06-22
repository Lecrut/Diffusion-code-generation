def find_largest_value(dictionary):
    if not dictionary:
        return None
    return max(dictionary.values())

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 5, 'c': 2}
    print(find_largest_value(sample_dict))