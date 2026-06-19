class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def validate_lengths(self):
        if not isinstance(self.length1, (int, float)) or not isinstance(self.length2, (int, float)):
            raise ValueError("Both lengths must be numbers (int or float).")

    def analyze(self):
        self.validate_lengths()
        if self.length1 > self.length2:
            print(f"{self.length1} is greater than {self.length2}")
        elif self.length1 < self.length2:
            print(f"{self.length1} is smaller than {self.length2}")
        else:
            print(f"{self.length1} is equal to {self.length2}")

if __name__ == '__main__':
    comparator = LengthComparator(5.6, 3.4)
    comparator.analyze()