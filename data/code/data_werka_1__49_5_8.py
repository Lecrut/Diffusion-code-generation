class LengthComparator:

    def __init__(self, len1, len2):
        self.len1 = len1
        self.len2 = len2

    def compare(self):
        if self.len1 == self.len2:
            return 'equal'
        elif self.len1 > self.len2:
            return 'len1 is greater'
        else:
            return 'len2 is smaller'
if __name__ == '__main__':
    comparator = LengthComparator(30, 45)
    result = comparator.compare()
    print(result)
    comparator2 = LengthComparator(50, 50)
    print(comparator2.compare())
    comparator3 = LengthComparator(25, 75)
    print(comparator3.compare())