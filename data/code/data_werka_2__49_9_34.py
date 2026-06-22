class LengthComparator:
    def __init__(self, length1, length2):
        self.lengths = {'first': length1, 'second': length2}
    
    def analyze(self):
        if self.lengths['first'] > self.lengths['second']:
            print(f"The first length ({self.lengths['first']}) is greater than the second length ({self.lengths['second']}).")
        elif self.lengths['first'] < self.lengths['second']:
            print(f"The first length ({self.lengths['first']}) is smaller than the second length ({self.lengths['second']}).")
        else:
            print(f"Both lengths are equal: {self.lengths['first']}.")

if __name__ == '__main__':
    comparator = LengthComparator(25, 30)
    comparator.analyze()