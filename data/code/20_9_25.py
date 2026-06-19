class ItemComparer:

    def check_equality(self, a, b):
        if type(a) != type(b):
            return False
        if isinstance(a, dict):
            return self._compare_dicts(a, b)
        elif isinstance(a, list):
            return self._compare_lists(a, b)
        else:
            return a == b

    def _compare_dicts(self, d1, d2):
        if len(d1) != len(d2):
            return False
        for key in d1:
            if key not in d2 or not self.check_equality(d1[key], d2[key]):
                return False
        return True

    def _compare_lists(self, l1, l2):
        if len(l1) != len(l2):
            return False
        for item1, item2 in zip(l1, l2):
            if not self.check_equality(item1, item2):
                return False
        return True
if __name__ == '__main__':
    comparer = ItemComparer()
    sample_dict1 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    sample_dict2 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    sample_dict3 = {'a': 1, 'b': [2, 3], 'c': {'d': 5}}
    print(comparer.check_equality(sample_dict1, sample_dict2))
    print(comparer.check_equality(sample_dict1, sample_dict3))
    sample_list1 = [1, [2, 3], {'a': 4}]
    sample_list2 = [1, [2, 3], {'a': 4}]
    sample_list3 = [1, [2, 3], {'a': 5}]
    print(comparer.check_equality(sample_list1, sample_list2))
    print(comparer.check_equality(sample_list1, sample_list3))