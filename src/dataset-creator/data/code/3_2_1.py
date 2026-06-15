class DivisionByZeroError(Exception):
    pass
class RatioCalculator:
    def calculate_division(self, numerator, denominator):
        if denominator == 0:
            raise DivisionByZeroError("Denominator cannot be zero")
        return numerator / denominator
if __name__ == '__main__':
    calculator = RatioCalculator()
    try:
        result1 = calculator.calculate_division(10, 2)
        print(f"10 / 2 = {result1}")
        result2 = calculator.calculate_division(15, 3)
        print(f"15 / 3 = {result2}")
        result3 = calculator.calculate_division(10, 0)
    except DivisionByZeroError as e:
        print(f"Error caught: {e}")