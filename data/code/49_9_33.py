class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2
        self.validate_lengths()

    def validate_lengths(self):
        if not (isinstance(self.length1, (int, float)) and isinstance(self.length2, (int, float))):
            raise ValueError("Both lengths must be numbers.")

    def analyze(self):
        if self.length1 > self.length2:
            print(f"{self.length1} is greater than {self.length2}")
        elif self.length1 < self.length2:
            print(f"{self.length1} is smaller than {self.length2}")
        else:
            print(f"{self.length1} is equal to {self.length2}")

if __name__ == '__main__':
    try:
        comparator = LengthComparator(7.5, 7.5)
        comparator.analyze()
    except ValueError as e:
        print(e)