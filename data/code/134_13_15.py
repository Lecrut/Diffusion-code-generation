class DictionaryChecker:

    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2

    def are_keys_disjoint(self):
        set1 = set(self.dict1.keys())
        set2 = set(self.dict2.keys())
        return set1.isdisjoint(set2)
if __name__ == '__main__':
    checker = DictionaryChecker({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
    print(checker.are_keys_disjoint())
    checker = DictionaryChecker({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    print(checker.are_keys_disjoint())