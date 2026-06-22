class LengthComparator:

    def __init__(self, length1, length2):
        try:
            self.length1 = float(length1)
            self.length2 = float(length2)
        except ValueError as e:
            raise ValueError('Both lengths must be valid numbers.') from e

    def compare(self):
        if self.length1 < self.length2:
            return 'First length is less than the second.'
        elif self.length1 > self.length2:
            return 'First length is greater than the second.'
        else:
            return 'Both lengths are equal.'
if __name__ == '__main__':
    try:
        comparator1 = LengthComparator(5, 10)
        print(comparator1.compare())
        comparator2 = LengthComparator(10, 5)
        print(comparator2.compare())
        comparator3 = LengthComparator(7, 7)
        print(comparator3.compare())
        comparator4 = LengthComparator('a', 8)
    except ValueError as e:
        print(e)