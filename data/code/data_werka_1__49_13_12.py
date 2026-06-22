class LengthCalculator:
    def __init__(self, length1, length2):
        if length1 == 0 or length2 == 0:
            raise ValueError("Lengths cannot be zero")
        self.length1 = length1
        self.length2 = length2

    def calculate_ratio(self):
        return self.length1 / self.length2

if __name__ == '__main__':
    length1 = 15.6789
    length2 = 3.4567
    calculator = LengthCalculator(length1, length2)
    ratio = calculator.calculate_ratio()
    print(f"The ratio of the lengths is: {ratio:.10f}")