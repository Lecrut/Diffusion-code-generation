class LengthComparator:
    EPSILON = 1e-9

    @staticmethod
    def are_equal(length1, length2):
        return abs(length1 - length2) < LengthComparator.EPSILON

    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def get_greater_length(self):
        if LengthComparator.are_equal(self.length1, self.length2):
            return None
        elif self.length1 > self.length2:
            return self.length1
        else:
            return self.length2

if __name__ == '__main__':
    comparator1 = LengthComparator(10.000000005, 10.0)
    print("Comparison 1:")
    print(comparator1.get_greater_length())

    comparator2 = LengthComparator(20, 20.000000001)
    print("\nComparison 2:")
    print(comparator2.get_greater_length())

    comparator3 = LengthComparator(5, 10)
    print("\nComparison 3:")
    print(comparator3.get_greater_length())