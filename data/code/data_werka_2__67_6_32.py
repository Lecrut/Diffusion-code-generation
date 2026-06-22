class SumCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def validate_attributes(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise ValueError("Both attributes must be numbers")

    def calculate_sum(self):
        self.validate_attributes()
        return self.a + self.b

if __name__ == '__main__':
    calculator = SumCalculator(12, 8)
    result = calculator.calculate_sum()
    print(result)