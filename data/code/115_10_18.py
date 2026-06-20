class Calculator:
    DIVISION_ERROR_MESSAGE = "Error: Division by zero is not allowed."

    @staticmethod
    def divide(num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print(Calculator.DIVISION_ERROR_MESSAGE)
            return None

if __name__ == '__main__':
    calculator = Calculator()
    result = calculator.divide(20.5, 4.2)
    if result is not None:
        print(result)