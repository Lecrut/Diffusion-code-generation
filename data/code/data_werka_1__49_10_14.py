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
    comparator1 = LengthComparator(5.6, 3.4)
    comparator1.analyze()

    comparator2 = LengthComparator(7.8, 7.8)
    comparator2.analyze()

    comparator3 = LengthComparator(2.9, 4.1)
    comparator3.analyze()