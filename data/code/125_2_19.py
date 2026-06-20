class MathOperations:
    ADD = 'add'
    SUBTRACT = 'subtract'

    @staticmethod
    def perform_operation(operation, a, b):
        if operation == MathOperations.ADD:
            return a + b
        elif operation == MathOperations.SUBTRACT:
            return a - b
        else:
            raise ValueError("Unsupported operation")

if __name__ == '__main__':
    result_add = MathOperations.perform_operation(MathOperations.ADD, 5, 3)
    print(result_add)

    result_subtract = MathOperations.perform_operation(MathOperations.SUBTRACT, 10, 4)
    print(result_subtract)