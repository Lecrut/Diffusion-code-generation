class ItemComparer:

    def check_equality(self, a, b):
        if type(a) != type(b):
            return False
        if isinstance(a, dict):
            if len(a) != len(b):
                return False
            for key in a:
                if key not in b or not self.check_equality(a[key], b[key]):
                    return False
            return True
        elif isinstance(a, list):
            if len(a) != len(b):
                return False
            for item1, item2 in zip(a, b):
                if not self.check_equality(item1, item2):
                    return False
            return True
        else:
            return a == b
if __name__ == '__main__':
    comparer = ItemComparer()
    dict1 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    dict2 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    dict3 = {'a': 1, 'b': [2, 3], 'c': {'d': 5}}
    list1 = [1, [2, 3], {'a': 4}]
    list2 = [1, [2, 3], {'a': 4}]
    list3 = [1, [2, 3], {'a': 5}]
    print(comparer.check_equality(dict1, dict2))
    print(comparer.check_equality(dict1, dict3))
    print(comparer.check_equality(list1, list2))
    print(comparer.check_equality(list1, list3))