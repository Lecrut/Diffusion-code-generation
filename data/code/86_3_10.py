class BoolComparator:
    @staticmethod
    def compare_booleans(a, b):
        return [a == b]

if __name__ == '__main__':
    comparator = BoolComparator()
    print(comparator.compare_booleans(True, False))
    print(comparator.compare_booleans(True, True))
    print(comparator.compare_booleans(False, True))