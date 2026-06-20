class DateCalculator:
    def calculate_month_diff(self, month1, month2):
        return abs(month2 - month1)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.calculate_month_diff(3, 8))