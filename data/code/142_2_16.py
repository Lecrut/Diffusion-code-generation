class BooleanComparator:
    def compare_booleans(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare_booleans(True, True))
    print(comparator.compare_booleans(False, False))
    print(comparator.compare_booleans(True, False))
    print(comparator.compare_booleans(False, True))