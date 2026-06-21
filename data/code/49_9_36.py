class LengthComparator:
    def __init__(self, length1, length2):
        self.lengths = [length1, length2]

    def analyze(self):
        if self.lengths[0] > self.lengths[1]:
            print(f"{self.lengths[0]} is greater than {self.lengths[1]}")
        elif self.lengths[0] < self.lengths[1]:
            print(f"{self.lengths[0]} is smaller than {self.lengths[1]}")
        else:
            print(f"{self.lengths[0]} is equal to {self.lengths[1]}")

if __name__ == '__main__':
    comparator = LengthComparator(7.5, 2.8)
    comparator.analyze()