class BooleanComparator:
    @staticmethod
    def compare(a, b):
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    result1 = comparator.compare(True, True)
    result2 = comparator.compare(False, False)
    print(result1 and result2)