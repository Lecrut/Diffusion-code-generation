class DictComparator:
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2

    def find_only_in_dict(self, dict1, dict2):
        return {k: v for k, v in dict1.items() if k not in dict2}

    def find_diff_values(self, dict1, dict2):
        common_keys = set(dict1) & set(dict2)
        return {k: (dict1[k], dict2[k]) for k in common_keys if dict1[k] != dict2[k]}

    def compare_dicts(self):
        only_in_dict1 = self.find_only_in_dict(self.dict1, self.dict2)
        only_in_dict2 = self.find_only_in_dict(self.dict2, self.dict1)
        diff_values = self.find_diff_values(self.dict1, self.dict2)
        return only_in_dict1, only_in_dict2, diff_values

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    comparator = DictComparator(sample_dict1, sample_dict2)
    result = comparator.compare_dicts()
    print(result)