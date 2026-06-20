class DateCalculator:
    def calculate_month_diff(self, month1: int, month2: int) -> int:
        return abs(month1 - month2)

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.calculate_month_diff(7, 3)
    print(result)