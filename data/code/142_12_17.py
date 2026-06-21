class BooleanComparator:
    @staticmethod
    def compare_booleans(a: bool, b: bool) -> bool:
        return not (a ^ b)

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare_booleans(True, True))
    print(comparator.compare_booleans(True, False))
    print(comparator.compare_booleans(False, False))
    print(comparator.compare_booleans(False, True))