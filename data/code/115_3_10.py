class DivisionCalculator:
    @staticmethod
    def divide(numerator, denominator):
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise TypeError("Both inputs must be numeric.")
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return numerator / denominator

if __name__ == '__main__':
    calculator = DivisionCalculator()
    num1 = 25
    num2 = 5
    result = calculator.divide(num1, num2)
    print(f"Result of {num1} divided by {num2}: {result}")
    num3 = 7.0
    num4 = 2.5
    result2 = calculator.divide(num3, num4)
    print(f"Result of {num3} divided by {num4}: {result2}")