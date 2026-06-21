class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def analyze(self):
        result = self.compare_lengths()
        print(result)

    @staticmethod
    def compare_lengths(length1, length2):
        if length1 > length2:
            return f"{length1} is greater than {length2}"
        elif length1 < length2:
            return f"{length1} is smaller than {length2}"
        else:
            return f"{length1} is equal to {length2}"

if __name__ == '__main__':
    comparator = LengthComparator(7.5, 7.5)
    comparator.analyze()