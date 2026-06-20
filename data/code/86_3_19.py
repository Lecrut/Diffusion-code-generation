class BooleanComparator:
    @staticmethod
    def compare_booleans(a, b):
        return [a == b]

if __name__ == '__main__':
    comparator = BooleanComparator()
    result1 = comparator.compare_booleans(True, False)
    print(result1)
    result2 = comparator.compare_booleans(True, True)
    print(result2)
    result3 = comparator.compare_booleans(False, True)
    print(result3)