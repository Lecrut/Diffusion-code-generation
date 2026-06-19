class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise ValueError("Length cannot be negative")
        if self.length1 == self.length2:
            return "Lengths are equal"
        elif self.length1 > self.length2:
            return f"First length ({self.length1}) is greater than second length ({self.length2})"
        else:
            return f"Second length ({self.length2}) is greater than first length ({self.length1})"

if __name__ == '__main__':
    comparator = LengthComparator(5, 3)
    try:
        result = comparator.compare_lengths()
        print(result)
    except ValueError as e:
        print(e)