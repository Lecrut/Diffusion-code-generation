class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise ValueError("Length cannot be negative")
        elif abs(self.length1 - self.length2) > 10:
            raise Exception("Lengths are impossibly different")

if __name__ == '__main__':
    length_comparator = LengthComparator(5, 16)
    try:
        length_comparator.compare_lengths()
    except Exception as e:
        print(e)