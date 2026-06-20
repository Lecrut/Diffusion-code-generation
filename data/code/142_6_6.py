class BooleanComparator:
    TRUE = True
    FALSE = False

    @staticmethod
    def fast_compare(a, b):
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.fast_compare(True, True))
    print(comparator.fast_compare(False, False))
    print(comparator.fast_compare(True, False))