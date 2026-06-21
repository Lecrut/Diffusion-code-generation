class DictComparator:
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2

    def compare(self):
        only_in_dict1 = {k: v for k, v in self.dict1.items() if k not in self.dict2}
        only_in_dict2 = {k: v for k, v in self.dict2.items() if k not in self.dict1}
        diff_values = {k: (self.dict1[k], self.dict2[k]) for k in set(self.dict1) & set(self.dict2) if self.dict1[k] != self.dict2[k]}
        return only_in_dict1, only_in_dict2, diff_values

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    comparator = DictComparator(sample_dict1, sample_dict2)
    result = comparator.compare()
    print(result)