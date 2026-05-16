class DivisionCalculator:
    def divide(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numeric.")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
if __name__ == '__main__':
    calculator = DivisionCalculator()
    num1 = 20
    num2 = 5
    result = calculator.divide(num1, num2)
    print(f"Result of {num1} divided by {num2}: {result}")
    num3 = 10
    num4 = 3
    result2 = calculator.divide(num3, num4)
    print(f"Result of {num3} divided by {num4}: {result2}")
    try:
        calculator.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
    try:
        calculator.divide(10, "a")
    except TypeError as e:
        print(f"Error caught: {e}")