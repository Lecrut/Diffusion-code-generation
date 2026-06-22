class ItemComparer:

    def check_equality(self, a, b):
        if isinstance(a, dict) and isinstance(b, dict):
            return self._compare_dicts(a, b)
        elif isinstance(a, list) and isinstance(b, list):
            return self._compare_lists(a, b)
        else:
            return a == b

    def _compare_dicts(self, dict1, dict2):
        if len(dict1) != len(dict2):
            return False
        for key in dict1:
            if key not in dict2 or not self.check_equality(dict1[key], dict2[key]):
                return False
        return True

    def _compare_lists(self, list1, list2):
        if len(list1) != len(list2):
            return False
        for item1, item2 in zip(list1, list2):
            if not self.check_equality(item1, item2):
                return False
        return True
if __name__ == '__main__':
    comparer = ItemComparer()
    dict_a = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    dict_b = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    list_a = [1, 2, [3, 4]]
    list_b = [1, 2, [3, 4]]
    print(comparer.check_equality(dict_a, dict_b))
    print(comparer.check_equality(list_a, list_b))
    print(comparer.check_equality(dict_a, list_a))