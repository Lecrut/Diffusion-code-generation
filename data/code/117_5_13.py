class NumberCalculator:
    ERROR_MESSAGE = "Both arguments must be numbers"

    @staticmethod
    def subtract_numbers(num1, num2):
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError(NumberCalculator.ERROR_MESSAGE)
        return num1 - num2

if __name__ == '__main__':
    calculator = NumberCalculator()
    result = calculator.subtract_numbers(100, 35)
    print(result)