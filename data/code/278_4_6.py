def print_dict_pairs(dictionary):
    if not isinstance(dictionary, dict) or not dictionary:
        raise ValueError("Input must be a non-empty dictionary")
    
    for key, value in dictionary.items():
        print(f'Key: {key}, Value: {value}')

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print_dict_pairs(sample_dict)