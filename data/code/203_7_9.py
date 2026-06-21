class BooleanComparator:
    def compare_booleans(self, a: bool, b: bool) -> int:
        return int(a != b)

if __name__ == '__main__':
    comparator = BooleanComparator()
    result1 = comparator.compare_booleans(True, False)
    result2 = comparator.compare_booleans(False, False)
    print(result1, result2)