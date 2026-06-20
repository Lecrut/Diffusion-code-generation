class MathOperations:
    def divide_and_round(self, dividend, divisor, decimal_places):
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return round(dividend / divisor, decimal_places)

if __name__ == '__main__':
    calculator = MathOperations()
    result1 = calculator.divide_and_round(10, 3, 2)
    print(result1)
    result2 = calculator.divide_and_round(100, 7, 3)
    print(result2)