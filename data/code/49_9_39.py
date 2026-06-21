class LengthComparator:
    def __init__(self, length1, length2):
        self.lengths = {'length1': length1, 'length2': length2}

    def analyze(self):
        if self.lengths['length1'] > self.lengths['length2']:
            print(f"{self.lengths['length1']} is greater than {self.lengths['length2']}")
        elif self.lengths['length1'] < self.lengths['length2']:
            print(f"{self.lengths['length1']} is smaller than {self.lengths['length2']}")
        else:
            print(f"{self.lengths['length1']} is equal to {self.lengths['length2']}")

if __name__ == '__main__':
    comparator = LengthComparator(7.5, 10)
    comparator.analyze()