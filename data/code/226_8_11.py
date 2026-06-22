def repeat_dict_keys(d):
    return [key for key in d.keys()] * 5

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(repeat_dict_keys(sample_dict))