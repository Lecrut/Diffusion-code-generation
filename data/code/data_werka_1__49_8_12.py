class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        try:
            result = self.length1 < self.length2
            return f"Length 1 ({self.length1}) is less than Length 2 ({self.length2}): {result}"
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    comparator1 = LengthComparator(5, 10)
    print(comparator1.compare())
    
    comparator2 = LengthComparator(10, 5)
    print(comparator2.compare())
    
    comparator3 = LengthComparator(7, 7)
    print(comparator3.compare())
    
    comparator4 = LengthComparator(3, 8)
    print(comparator4.compare())