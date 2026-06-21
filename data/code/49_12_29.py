class LengthCalculator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def calculate_ratio(self):
        if self.length2 == 0:
            raise ValueError("Length2 cannot be zero.")
        return self.length1 / self.length2

if __name__ == '__main__':
    length1 = 12.3456
    length2 = 4.5678
    calculator = LengthCalculator(length1, length2)
    try:
        ratio = calculator.calculate_ratio()
        print(f"The ratio of {length1} to {length2} is: {ratio:.10f}")
    except ValueError as e:
        print(e)