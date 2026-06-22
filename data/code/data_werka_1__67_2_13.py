class MathOperations:
    ADDITION = "addition"

    @staticmethod
    def perform_operation(operation, *args):
        if operation == MathOperations.ADDITION:
            return sum(args)
        else:
            raise ValueError("Unsupported operation")

if __name__ == '__main__':
    num1 = 7.5
    num2 = 4.8
    result = MathOperations.perform_operation(MathOperations.ADDITION, num1, num2)
    print(result)