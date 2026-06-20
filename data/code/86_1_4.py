class BoolComparator:
    def compare_booleans(self, a: bool, b: bool) -> str:
        return 'True' if a == b else 'False'

if __name__ == '__main__':
    comparator = BoolComparator()
    print(comparator.compare_booleans(True, True))
    print(comparator.compare_booleans(False, False))
    print(comparator.compare_booleans(True, False))
    print(comparator.compare_booleans(False, True))