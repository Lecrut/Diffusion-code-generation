class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        try:
            if not isinstance(self.length1, (int, float)) or not isinstance(self.length2, (int, float)):
                raise ValueError("Both lengths must be numbers.")
            return self.length1 < self.length2
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    comparator1 = LengthComparator(5, 10)
    print(comparator1.compare())
    comparator2 = LengthComparator(10, 5)
    print(comparator2.compare())
    comparator3 = LengthComparator(7, 7)
    print(comparator3.compare())
    comparator4 = LengthComparator(3.5, 2.8)
    print(comparator4.compare())
    comparator5 = LengthComparator('a', 10)
    print(comparator5.compare())