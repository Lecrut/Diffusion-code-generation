class LengthCalculator:
    def __init__(self, length1, length2):
        if length1 <= 0 or length2 <= 0:
            raise ValueError("Lengths must be positive numbers")
        self.length1 = length1
        self.length2 = length2

    def calculate_difference(self):
        return abs(self.length1 - self.length2)

    def calculate_ratio(self):
        return max(self.length1, self.length2) / min(self.length1, self.length2)

    def get_results(self):
        difference = self.calculate_difference()
        ratio = self.calculate_ratio()
        return {
            'original_lengths': (self.length1, self.length2),
            'difference': difference,
            'ratio': ratio
        }

if __name__ == '__main__':
    length_calculator = LengthCalculator(10, 5)
    print(length_calculator.get_results())