class LengthComparator:
    def __init__(self, length1, length2):
        self.lengths = {'Length 1': length1, 'Length 2': length2}

    def analyze(self):
        if self.lengths['Length 1'] > self.lengths['Length 2']:
            print(f"{self.lengths['Length 1']} is greater than {self.lengths['Length 2']}")
        elif self.lengths['Length 1'] < self.lengths['Length 2']:
            print(f"{self.lengths['Length 1']} is smaller than {self.lengths['Length 2']}")
        else:
            print(f"{self.lengths['Length 1']} is equal to {self.lengths['Length 2']}")

if __name__ == '__main__':
    comparator = LengthComparator(30.5, 14.7)
    comparator.analyze()