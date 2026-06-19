class ItemComparer:

    def check_equality(self, a, b):
        if type(a) != type(b):
            return False
        if isinstance(a, (int, float, str, bool)):
            return a == b
        elif isinstance(a, list):
            if len(a) != len(b):
                return False
            for item_a, item_b in zip(a, b):
                if not self.check_equality(item_a, item_b):
                    return False
            return True
        elif isinstance(a, dict):
            if a.keys() != b.keys():
                return False
            for key in a:
                if not self.check_equality(a[key], b[key]):
                    return False
            return True
        else:
            raise TypeError('Unsupported type')
if __name__ == '__main__':
    comparer = ItemComparer()
    sample1 = [1, 2, [3, 4]]
    sample2 = [1, 2, [3, 4]]
    sample3 = {'a': 1, 'b': {'c': 2}}
    sample4 = {'a': 1, 'b': {'c': 3}}
    print(comparer.check_equality(sample1, sample2))
    print(comparer.check_equality(sample3, sample4))