class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def analyze(self):
        if self.length1 > self.length2:
            return f"{self.length1} is greater than {self.length2}"
        elif self.length1 < self.length2:
            return f"{self.length1} is smaller than {self.length2}"
        else:
            return f"{self.length1} is equal to {self.length2}"

if __name__ == '__main__':
    comparator = LengthComparator(5.5, 3.2)
    print(comparator.analyze())

    comparator2 = LengthComparator(7.7, 7.7)
    print(comparator2.analyze())

    comparator3 = LengthComparator(10.0, 12.5)
    print(comparator3.analyze())