class ItemComparer:

    def check_equality(self, a, b):
        if isinstance(a, dict) and isinstance(b, dict):
            return self.compare_dicts(a, b)
        elif isinstance(a, list) and isinstance(b, list):
            return self.compare_lists(a, b)
        else:
            return a == b

    def compare_dicts(self, d1, d2):
        if len(d1) != len(d2):
            return False
        for key in d1:
            if key not in d2 or not self.check_equality(d1[key], d2[key]):
                return False
        return True

    def compare_lists(self, l1, l2):
        if len(l1) != len(l2):
            return False
        for item1, item2 in zip(l1, l2):
            if not self.check_equality(item1, item2):
                return False
        return True
if __name__ == '__main__':
    comparer = ItemComparer()
    dict1 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    dict2 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    dict3 = {'a': 1, 'b': [2, 3], 'c': {'d': 5}}
    list1 = [1, {'x': 2}, [3, 4]]
    list2 = [1, {'x': 2}, [3, 4]]
    list3 = [1, {'x': 2}, [3, 5]]
    print(comparer.check_equality(dict1, dict2))
    print(comparer.check_equality(dict1, dict3))
    print(comparer.check_equality(list1, list2))
    print(comparer.check_equality(list1, list3))