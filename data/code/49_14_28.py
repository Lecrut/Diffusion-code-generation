def compare_lengths(length1, length2):
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise ValueError("Both lengths must be numbers")
    return max(length1, length2)

class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def get_longer_length(self):
        try:
            return compare_lengths(self.length1, self.length2)
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    sample_length1 = 35.4
    sample_length2 = 28.9
    comparator = LengthComparator(sample_length1, sample_length2)
    longer_length = comparator.get_longer_length()
    print(longer_length)