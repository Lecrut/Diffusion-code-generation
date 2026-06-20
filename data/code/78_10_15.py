class DateCalculator:
    MONTHS_PER_YEAR = 12

    def calculate_month_diff(self, month1: int, month2: int) -> int:
        return abs((month2 - month1 + self.MONTHS_PER_YEAR) % self.MONTHS_PER_YEAR)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.calculate_month_diff(5, 10))