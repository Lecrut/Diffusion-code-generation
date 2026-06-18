class DivisionByZeroError(Exception):
    pass
class RatioCalculator:
    def calculate_division(self, numerator, denominator):
        if denominator == 0:
            raise DivisionByZeroError("Error: Cannot divide by zero.")
        return numerator / denominator
if __name__ == '__main__':
    calculator = RatioCalculator()
    numerator1 = 10
    denominator1 = 2
    try:
        result1 = calculator.calculate_division(numerator1, denominator1)
        print(f"Result of {numerator1} / {denominator1}: {result1}")
    except DivisionByZeroError as e:
        print(e)
    numerator2 = 15
    denominator2 = 0
    try:
        result2 = calculator.calculate_division(numerator2, denominator2)
        print(f"Result of {numerator2} / {denominator2}: {result2}")
    except DivisionByZeroError as e:
        print(e)