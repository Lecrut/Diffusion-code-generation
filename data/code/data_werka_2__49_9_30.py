class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def analyze(self):
        if self.length1 > self.length2:
            result = f"{self.length1} is greater than {self.length2}"
        elif self.length1 < self.length2:
            result = f"{self.length1} is smaller than {self.length2}"
        else:
            result = f"{self.length1} is equal to {self.length2}"
        print(result)

if __name__ == '__main__':
    length_a = 7.0
    length_b = 7.0
    comparator = LengthComparator(length_a, length_b)
    comparator.analyze()