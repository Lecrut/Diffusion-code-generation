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
    LENGTH1 = 10.0
    LENGTH2 = 5.0

    calculator = LengthCalculator(LENGTH1, LENGTH2)
    difference = calculator.calculate_difference()
    ratio = calculator.calculate_ratio()

    result = {
        "original_lengths": {"length1": LENGTH1, "length2": LENGTH2},
        "difference": difference,
        "ratio": ratio
    }

    print(result)