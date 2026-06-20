class BooleanComparator:
    def compare(self, a: bool, b: bool) -> int:
        return (a - b) & 1

if __name__ == '__main__':
    comparator = BooleanComparator()
    result1 = comparator.compare(True, True)
    print(result1)
    result2 = comparator.compare(False, False)
    print(result2)
    result3 = comparator.compare(True, False)
    print(result3)
    result4 = comparator.compare(False, True)
    print(result4)