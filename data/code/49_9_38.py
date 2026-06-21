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
    length_comparator = LengthComparator(10, 20)
    length_comparator.analyze()

    length_comparator = LengthComparator(30, 30)
    length_comparator.analyze()

    length_comparator = LengthComparator(40, 25)
    length_comparator.analyze()