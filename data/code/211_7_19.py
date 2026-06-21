class DictComparator:
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2

    def keys_only_in_dict1(self):
        return {k: v for k, v in self.dict1.items() if k not in self.dict2}

    def keys_only_in_dict2(self):
        return {k: v for k, v in self.dict2.items() if k not in self.dict1}

    def differing_values(self):
        return {k: (self.dict1[k], self.dict2[k]) for k in set(self.dict1) & set(self.dict2) if self.dict1[k] != self.dict2[k]}

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    comparator = DictComparator(sample_dict1, sample_dict2)
    print(comparator.keys_only_in_dict1())
    print(comparator.keys_only_in_dict2())
    print(comparator.differing_values())