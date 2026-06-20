class Calculator:
    ADD = 'add'
    SUBTRACT = 'subtract'

    @staticmethod
    def calculate(operation, a, b):
        if operation == Calculator.ADD:
            return a + b
        elif operation == Calculator.SUBTRACT:
            return a - b
        else:
            raise ValueError("Invalid operation specified")

if __name__ == '__main__':
    result_add = Calculator.calculate(Calculator.ADD, 10, 5)
    result_subtract = Calculator.calculate(Calculator.SUBTRACT, 10, 5)
    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")