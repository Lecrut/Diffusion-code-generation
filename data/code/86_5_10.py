class BooleanComparator:
    def compare(self, a: bool, b: bool) -> tuple:
        return (a == b), '=='

if __name__ == '__main__':
    comparator = BooleanComparator()
    result1 = comparator.compare(True, False)
    print(result1)
    result2 = comparator.compare(False, False)
    print(result2)
    result3 = comparator.compare(True, True)
    print(result3)