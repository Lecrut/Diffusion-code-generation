class MonthDifferenceCalculator:
    def calculate_months_elapsed(self, start_month, end_month):
        return abs(end_month - start_month)

if __name__ == '__main__':
    calculator = MonthDifferenceCalculator()
    print(calculator.calculate_months_elapsed(1, 5))
    print(calculator.calculate_months_elapsed(10, 3))
    print(calculator.calculate_months_elapsed(12, 12))