class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise ValueError("Length cannot be negative")
        if abs(self.length1 - self.length2) > 1:
            raise ValueError("Lengths are impossibly different")

if __name__ == '__main__':
    comparator = LengthComparator(5, 6)
    try:
        comparator.compare_lengths()
        print("Lengths are comparable.")
    except ValueError as e:
        print(e)