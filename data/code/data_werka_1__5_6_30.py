class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise ValueError("Length cannot be negative")
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    try:
        comparator = LengthComparator(5, -3)
        result = comparator.compare_lengths()
        print(result)
    except ValueError as e:
        print(e)