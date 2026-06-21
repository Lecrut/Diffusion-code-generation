class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def validate_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise ValueError("Lengths cannot be negative")

    def compare_lengths(self):
        self.validate_lengths()
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    try:
        comparator = LengthComparator(-5, 3)
        difference = comparator.compare_lengths()
        print(difference)
    except ValueError as e:
        print(e)