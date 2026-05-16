class DateCalculator:
    def calculate_month_diff(self, month1, month2):
        return abs(month1 - month2)
if __name__ == '__main__':
    calculator = DateCalculator()
    month_a = 5
    month_b = 10
    difference = calculator.calculate_month_diff(month_a, month_b)
    print(difference)