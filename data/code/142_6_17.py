class BoolComparator:
    TRUE = True
    FALSE = False

    @staticmethod
    def fast_bool_compare(a, b):
        return a == b

if __name__ == '__main__':
    comparator = BoolComparator()
    print(comparator.fast_bool_compare(True, True))
    print(comparator.fast_bool_compare(False, False))
    print(comparator.fast_bool_compare(True, False))