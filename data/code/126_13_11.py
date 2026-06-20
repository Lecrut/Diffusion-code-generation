class DictComparator:

    @staticmethod
    def are_dicts_equal(d1, d2):
        if id(d1) == id(d2):
            return True
        if not isinstance(d1, dict) or not isinstance(d2, dict):
            return False
        if len(d1) != len(d2):
            return False
        for key in d1:
            if key not in d2 or not DictComparator.are_dicts_equal(d1[key], d2[key]):
                return False
        return True
if __name__ == '__main__':
    sample1 = {'a': 1, 'b': {'c': 2}}
    sample2 = {'a': 1, 'b': {'c': 2}}
    print(DictComparator.are_dicts_equal(sample1, sample2))
    sample3 = {'a': 1, 'b': {'c': 3}}
    sample4 = {'a': 1, 'b': {'c': 2}}
    print(DictComparator.are_dicts_equal(sample3, sample4))