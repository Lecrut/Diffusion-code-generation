class ArithmeticOperations:
    def __init__(self):
        self.base_value = 1234567890

    def subtract_from_base(self, value):
        return self.base_value - value

if __name__ == '__main__':
    calculator = ArithmeticOperations()
    result1 = calculator.subtract_from_base(987654321)
    result2 = calculator.subtract_from_base(1234567890)
    print(result1)
    print(result2)