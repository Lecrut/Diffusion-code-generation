class ArithmeticOperations:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.validate_and_compute('+')

    def subtract(self):
        return self.validate_and_compute('-')

    def validate_and_compute(self, operator):
        if operator == '+':
            return self.num1 + self.num2
        elif operator == '-':
            return self.num1 - self.num2
        else:
            raise ValueError('Unsupported operator')
if __name__ == '__main__':
    calc = ArithmeticOperations(5, 3)
    print(calc.add())
    print(calc.subtract())