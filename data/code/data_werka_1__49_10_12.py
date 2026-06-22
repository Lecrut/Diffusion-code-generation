class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def analyze(self):
        if self.length1 > self.length2:
            print(f"Length A ({self.length1}) is greater than Length B ({self.length2})")
        elif self.length1 < self.length2:
            print(f"Length A ({self.length1}) is smaller than Length B ({self.length2})")
        else:
            print(f"Length A ({self.length1}) is equal to Length B ({self.length2})")

if __name__ == '__main__':
    length_a = 25.7
    length_b = 30.4
    comparator = LengthComparator(length_a, length_b)
    comparator.analyze()