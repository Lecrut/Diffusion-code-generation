class LengthComparator:
    def __init__(self, length1, length2):
        self.lengths = {'Length A': length1, 'Length B': length2}

    def analyze(self):
        if self.lengths['Length A'] > self.lengths['Length B']:
            print(f"{self.lengths['Length A']} is greater than {self.lengths['Length B']}")
        elif self.lengths['Length A'] < self.lengths['Length B']:
            print(f"{self.lengths['Length A']} is smaller than {self.lengths['Length B']}")
        else:
            print(f"{self.lengths['Length A']} is equal to {self.lengths['Length B']}")

if __name__ == '__main__':
    comparator = LengthComparator(12.3, 45.6)
    comparator.analyze()