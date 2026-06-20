class BooleanComparator:
    @staticmethod
    def are_booleans_equal(a, b):
        return (not a) == (not b)

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.are_booleans_equal(True, True))
    print(comparator.are_booleans_equal(False, False))
    print(comparator.are_booleans_equal(True, False))