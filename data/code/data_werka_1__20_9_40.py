class ItemComparer:

    def check_equality(self, a, b):
        if isinstance(a, dict) and isinstance(b, dict):
            return self.compare_dicts(a, b)
        elif isinstance(a, list) and isinstance(b, list):
            return self.compare_lists(a, b)
        else:
            return a == b

    def compare_dicts(self, a, b):
        if len(a) != len(b):
            return False
        for key in a:
            if key not in b or not self.check_equality(a[key], b[key]):
                return False
        return True

    def compare_lists(self, a, b):
        if len(a) != len(b):
            return False
        for item_a, item_b in zip(a, b):
            if not self.check_equality(item_a, item_b):
                return False
        return True
if __name__ == '__main__':
    comparer = ItemComparer()
    dict1 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    dict2 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    list1 = [1, 2, [3, 4]]
    list2 = [1, 2, [3, 5]]
    print(comparer.check_equality(dict1, dict2))
    print(comparer.check_equality(list1, list2))