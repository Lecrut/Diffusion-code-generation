class ArithmeticOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract_numbers(num1, num2):
        return num1 - num2

if __name__ == '__main__':
    calculator = ArithmeticOperations(5, 3)
    print("Addition Result:", ArithmeticOperations.add_numbers(calculator.num1, calculator.num2))
    print("Subtraction Result:", ArithmeticOperations.subtract_numbers(calculator.num1, calculator.num2))