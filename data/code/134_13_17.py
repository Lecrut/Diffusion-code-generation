def are_keys_disjoint(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    return set1.isdisjoint(set2)
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2}
    sample_dict2 = {'c': 3, 'd': 4}
    print(are_keys_disjoint(sample_dict1, sample_dict2))
    sample_dict3 = {'a': 5, 'b': 6}
    sample_dict4 = {'b': 7, 'c': 8}
    print(are_keys_disjoint(sample_dict3, sample_dict4))