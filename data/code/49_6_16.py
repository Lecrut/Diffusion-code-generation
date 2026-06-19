class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        return 'len1 is greater' if self.length1 > self.length2 else 'len2 is smaller' if self.length1 < self.length2 else 'equal'

if __name__ == '__main__':
    comparator1 = LengthComparator(10, 5)
    print(comparator1.compare())

    comparator2 = LengthComparator(7, 7)
    print(comparator2.compare())

    comparator3 = LengthComparator(15, 20)
    print(comparator3.compare())