class DifferenceCalculator:
    def __init__(self, *values):
        self.values = values

    def compute_differences(self):
        return [abs(a - b) for a, b in zip(self.values, self.values[1:])]

if __name__ == '__main__':
    calculator = DifferenceCalculator(10, 5, 8, 2, 15)
    differences = calculator.compute_differences()
    for diff in differences:
        print(diff)