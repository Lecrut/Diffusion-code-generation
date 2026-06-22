class LengthCalculator:
    def __init__(self, length1, length2):
        if length1 == 0 or length2 == 0:
            raise ValueError("Lengths cannot be zero")
        self.length1 = length1
        self.length2 = length2

    def calculate_difference(self):
        return abs(self.length1 - self.length2)

    def calculate_ratio(self):
        return max(self.length1, self.length2) / min(self.length1, self.length2)

if __name__ == '__main__':
    length_calculator = LengthCalculator(10, 5)
    print("Difference:", length_calculator.calculate_difference())
    print("Ratio:", length_calculator.calculate_ratio())