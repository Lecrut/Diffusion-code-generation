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
    comparator1 = LengthComparator(10, 5)
    comparator1.analyze()
    comparator2 = LengthComparator(20, 20)
    comparator2.analyze()
    comparator3 = LengthComparator(3, 15)
    comparator3.analyze()