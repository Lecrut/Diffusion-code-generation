class RatioCalculator:
    def calculate_division(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
if __name__ == '__main__':
    calculator = RatioCalculator()
    result1 = calculator.calculate_division(10, 2)
    print(f"10 / 2 = {result1}")
    result2 = calculator.calculate_division(15, 3)
    print(f"15 / 3 = {result2}")
    result3 = calculator.calculate_division(7, 4)
    print(f"7 / 4 = {result3}")
    try:
        calculator.calculate_division(5, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")