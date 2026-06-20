class BooleanComparator:
    def __init__(self, bool1, bool2):
        self.bool1 = bool1
        self.bool2 = bool2

    def are_equal(self):
        return self.bool1 == self.bool2

if __name__ == '__main__':
    comparator1 = BooleanComparator(True, True)
    print(comparator1.are_equal())

    comparator2 = BooleanComparator(True, False)
    print(comparator2.are_equal())

    comparator3 = BooleanComparator(False, True)
    print(comparator3.are_equal())

    comparator4 = BooleanComparator(False, False)
    print(comparator4.are_equal())