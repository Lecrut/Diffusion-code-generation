class DateCalculator:
    def calculate_month_diff(self, month1, month2):
        return abs(month1 - month2)

if __name__ == '__main__':
    calculator = DateCalculator()
    months_ahead = calculator.calculate_month_diff(12, 3)
    print(months_ahead)