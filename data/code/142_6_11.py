class BoolComparator:
    @staticmethod
    def fast_compare(a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BoolComparator()
    print(comparator.fast_compare(True, True))
    print(comparator.fast_compare(False, False))
    print(comparator.fast_compare(True, False))