class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = float(length1)
        self.length2 = float(length2)

    def compare_lengths(self):
        if self.length1 > self.length2:
            return "Length 1 is greater than Length 2"
        elif self.length1 < self.length2:
            return "Length 1 is less than Length 2"
        else:
            return "Length 1 is equal to Length 2"

    def print_comparison(self):
        result = self.compare_lengths()
        print(f"Length 1: {self.length1}")
        print(f"Length 2: {self.length2}")
        print(f"Comparison Result: {result}")

if __name__ == '__main__':
    length_comparator = LengthComparator(5.5, 3.2)
    length_comparator.print_comparison()