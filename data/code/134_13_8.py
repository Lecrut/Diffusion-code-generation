def check_mutual_exclusivity(dict1, dict2):
    return set(dict1.keys()).isdisjoint(set(dict2.keys()))

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2}
    sample_dict2 = {'c': 3, 'd': 4}
    print(check_mutual_exclusivity(sample_dict1, sample_dict2))