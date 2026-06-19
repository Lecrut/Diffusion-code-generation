class SumCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def validate_inputs(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise ValueError("Inputs must be numbers")

    def calculate_sum(self):
        return self.a + self.b

if __name__ == '__main__':
    calculator = SumCalculator(15, 20)
    calculator.validate_inputs()
    result = calculator.calculate_sum()
    print(result)