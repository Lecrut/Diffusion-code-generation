class DivisionCalculator:
    def divide(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return numerator / denominator
if __name__ == '__main__':
    calculator = DivisionCalculator()
    num1 = 10
    den1 = 2
    result1 = calculator.divide(num1, den1)
    print(f"Result of {num1} divided by {den1}: {result1}")
    num2 = 15
    den2 = 3
    result2 = calculator.divide(num2, den2)
    print(f"Result of {num2} divided by {den2}: {result2}")
    num3 = 7
    den3 = 2
    result3 = calculator.divide(num3, den3)
    print(f"Result of {num3} divided by {den3}: {result3}")
    try:
        calculator.divide(5, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")