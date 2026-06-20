class DateCalculator:
    def calculate_month_diff(self, month1: int, month2: int) -> int:
        return abs(month1 - month2)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.calculate_month_diff(5, 10))