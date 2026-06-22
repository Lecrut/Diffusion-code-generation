class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def validate_lengths(self):
        if not (isinstance(self.length1, (int, float)) and isinstance(self.length2, (int, float))):
            raise ValueError("Both lengths must be numbers")

    def compare(self):
        self.validate_lengths()
        if self.length1 > self.length2:
            return f"{self.length1} is greater than {self.length2}"
        elif self.length1 < self.length2:
            return f"{self.length1} is less than {self.length2}"
        else:
            return f"{self.length1} is equal to {self.length2}"

if __name__ == '__main__':
    comparator1 = LengthComparator(10, 25)
    print(comparator1.compare())

    comparator2 = LengthComparator(50, 50)
    print(comparator2.compare())

    comparator3 = LengthComparator(100, 10)
    print(comparator3.compare())