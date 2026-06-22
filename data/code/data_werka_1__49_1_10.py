class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def _validate_lengths(self):
        if not isinstance(self.length1, (int, float)) or not isinstance(self.length2, (int, float)):
            raise ValueError("Both lengths must be numbers.")
        return True

    def compare(self):
        if self._validate_lengths():
            if self.length1 > self.length2:
                return f"{self.length1} is greater than {self.length2}"
            elif self.length1 < self.length2:
                return f"{self.length1} is less than {self.length2}"
            else:
                return f"{self.length1} is equal to {self.length2}"

if __name__ == '__main__':
    comparator1 = LengthComparator(10, 5)
    print(comparator1.compare())

    comparator2 = LengthComparator(20, 30)
    print(comparator2.compare())

    comparator3 = LengthComparator(45, 45)
    print(comparator3.compare())