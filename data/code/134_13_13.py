def are_keys_mutually_exclusive(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    return set1.isdisjoint(set2)
if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    print(are_keys_mutually_exclusive(dict1, dict2))