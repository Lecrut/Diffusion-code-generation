class LengthComparator:

    def __init__(self, km1, m1):
        self.total_m = km1 * 1000 + m1

    def compare_to(self, other):
        if self.total_m < other.total_m:
            return -1
        elif self.total_m > other.total_m:
            return 1
        else:
            return 0
if __name__ == '__main__':
    comparator1 = LengthComparator(5, 300)
    comparator2 = LengthComparator(4, 900)
    print(comparator1.compare_to(comparator2))
    comparator3 = LengthComparator(3, 500)
    comparator4 = LengthComparator(3, 500)
    print(comparator3.compare_to(comparator4))
    comparator5 = LengthComparator(2, 750)
    comparator6 = LengthComparator(3, 250)
    print(comparator5.compare_to(comparator6))