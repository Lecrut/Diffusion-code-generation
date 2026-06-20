class ArithmeticOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

if __name__ == '__main__':
    operation = ArithmeticOperations(5, 3)
    print("Addition:", ArithmeticOperations.add(operation.num1, operation.num2))
    print("Subtraction:", ArithmeticOperations.subtract(operation.num1, operation.num2))