class BoolComparator:
    @staticmethod
    def compare_booleans(a: bool, b: bool) -> str:
        return 'Equal' if a == b else 'Different'

if __name__ == '__main__':
    comparator = BoolComparator()
    print(comparator.compare_booleans(True, True))
    print(comparator.compare_booleans(False, False))
    print(comparator.compare_booleans(True, False))
    print(comparator.compare_booleans(False, True))