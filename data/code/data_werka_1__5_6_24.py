class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise ValueError("Lengths cannot be negative")
        elif abs(self.length1 - self.length2) > 10:
            raise ValueError("Lengths are impossibly different")
        return "Lengths are comparable"

if __name__ == '__main__':
    comparator = LengthComparator(5, 7)
    try:
        result = comparator.compare_lengths()
        print(result)
    except ValueError as e:
        print(e)