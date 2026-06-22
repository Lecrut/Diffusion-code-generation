class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare_lengths(self):
        if self.length1 > self.length2:
            return f"{self.length1} is greater than {self.length2}"
        elif self.length1 < self.length2:
            return f"{self.length1} is smaller than {self.length2}"
        else:
            return f"{self.length1} is equal to {self.length2}"

    def analyze(self):
        result = self.compare_lengths()
        print(result)

if __name__ == '__main__':
    length1_value = 7.5
    length2_value = 7.5
    comparator = LengthComparator(length1_value, length2_value)
    comparator.analyze()