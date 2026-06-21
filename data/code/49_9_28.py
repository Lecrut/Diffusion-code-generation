class LengthComparator:
    LESS_THAN = "is smaller than"
    GREATER_THAN = "is greater than"
    EQUAL_TO = "is equal to"

    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        if self.length1 > self.length2:
            return LengthComparator.GREATER_THAN
        elif self.length1 < self.length2:
            return LengthComparator.LESS_THAN
        else:
            return LengthComparator.EQUAL_TO

    def analyze(self):
        result = self.compare()
        print(f"{self.length1} {result} {self.length2}")

if __name__ == '__main__':
    comparator = LengthComparator(7, 3)
    comparator.analyze()