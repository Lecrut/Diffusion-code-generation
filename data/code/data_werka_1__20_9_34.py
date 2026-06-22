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
    a = {'key1': [1, 2, {'subkey': 'value'}], 'key2': 'value'}
    b = {'key1': [1, 2, {'subkey': 'value'}], 'key2': 'value'}
    c = {'key1': [1, 2, {'subkey': 'different'}], 'key2': 'value'}
    print(comparer.check_equality(a, b))
    print(comparer.check_equality(a, c))