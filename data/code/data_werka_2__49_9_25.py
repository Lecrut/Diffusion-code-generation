class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def analyze(self):
        if self.length1 > self.length2:
            print(f"{self.length1} is greater than {self.length2}")
        elif self.length1 < self.length2:
            print(f"{self.length1} is smaller than {self.length2}")
        else:
            print(f"{self.length1} is equal to {self.length2}")

if __name__ == '__main__':
    COMPARISON_LENGTH_1 = 25.0
    COMPARISON_LENGTH_2 = 30.0

    comparator = LengthComparator(COMPARISON_LENGTH_1, COMPARISON_LENGTH_2)
    comparator.analyze()