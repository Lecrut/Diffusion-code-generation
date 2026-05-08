class BooleanComparator:
    @staticmethod
    def compare_booleans(a: bool, b: bool) -> tuple[bool, tuple[bool, bool]]:
        same = a == b
        result = (same, a, b)
        return result
if __name__ == '__main__':
    print(BooleanComparator.compare_booleans(True, True))
    print(BooleanComparator.compare_booleans(False, False))
    print(BooleanComparator.compare_booleans(True, False))
    print(BooleanComparator.compare_booleans(False, True))