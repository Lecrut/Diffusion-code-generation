class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        if not isinstance(self.length1, (int, float)) or not isinstance(self.length2, (int, float)):
            raise ValueError("Both lengths must be numbers")
        return max(self.length1, self.length2)

if __name__ == '__main__':
    sample_length1 = 18.4
    sample_length2 = 13.6
    comparator = LengthComparator(sample_length1, sample_length2)
    longer_length = comparator.compare()
    print(longer_length)