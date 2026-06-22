def find_max_value(dictionary):
    return max(dictionary.values())

if __name__ == '__main__':
    sample_dict = {'a': 34, 'b': 67, 'c': 23}
    print(find_max_value(sample_dict))