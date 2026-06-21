def are_dicts_equal(dict1, dict2):
    return dict1.items() == dict2.items()

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2}
    sample_dict2 = {'b': 2, 'a': 1}
    print(are_dicts_equal(sample_dict1, sample_dict2))