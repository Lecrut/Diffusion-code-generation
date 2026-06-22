class LengthComparator:
    LENGTH_1 = 5.5
    LENGTH_2 = 3.3

    @staticmethod
    def compare_lengths(a, b):
        if a > b:
            return "Length 1 is greater than Length 2"
        elif a < b:
            return "Length 1 is less than Length 2"
        else:
            return "Length 1 is equal to Length 2"

    def __init__(self, length1=LENGTH_1, length2=LENGTH_2):
        self.length1 = length1
        self.length2 = length2

    def compare_and_print(self):
        result = self.compare_lengths(self.length1, self.length2)
        print(f"Length 1: {self.length1}")
        print(f"Length 2: {self.length2}")
        print(f"Comparison Result: {result}")

if __name__ == '__main__':
    comparator = LengthComparator()
    comparator.compare_and_print()