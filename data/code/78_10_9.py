class DateCalculator:
    def calculate_month_diff(self, month1: int, month2: int) -> int:
        return abs(month1 - month2)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.calculate_month_diff(10, 3))
    print(calculator.calculate_month_diff(5, 10))
    print(calculator.calculate_month_diff(7, 3))
    print(calculator.calculate_month_diff(5, 3))