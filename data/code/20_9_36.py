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
    sample1 = {'a': [1, 2, {'b': 3}], 'c': 4}
    sample2 = {'a': [1, 2, {'b': 3}], 'c': 4}
    sample3 = {'a': [1, 2, {'b': 4}], 'c': 4}
    print(comparer.check_equality(sample1, sample2))
    print(comparer.check_equality(sample1, sample3))