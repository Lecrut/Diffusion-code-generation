class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def analyze(self):
        if self.length1 > self.length2:
            return f"Length 1 ({self.length1}) is greater than Length 2 ({self.length2})"
        elif self.length1 < self.length2:
            return f"Length 1 ({self.length1}) is smaller than Length 2 ({self.length2})"
        else:
            return f"Length 1 ({self.length1}) is equal to Length 2 ({self.length2})"

if __name__ == '__main__':
    comparator = LengthComparator(10, 5)
    print(comparator.analyze())