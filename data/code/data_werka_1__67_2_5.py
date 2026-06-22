class ArithmeticOperations:
    ADDITION = "addition"

    @staticmethod
    def perform_operation(operation, a, b):
        if operation == ArithmeticOperations.ADDITION:
            return a + b
        else:
            raise ValueError("Unsupported operation")

if __name__ == '__main__':
    num1 = 7.5
    num2 = 4.25
    result = ArithmeticOperations.perform_operation(ArithmeticOperations.ADDITION, num1, num2)
    print(result)