class DateCalculator:
    MONTHS_PER_YEAR = 12

    @staticmethod
    def calculate_month_diff(month1, month2):
        return abs((month2 - month1) % DateCalculator.MONTHS_PER_YEAR)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.calculate_month_diff(5, 10))