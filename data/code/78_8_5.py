class MonthDifferenceCalculator:
    def find_month_difference(self, month1: int, month2: int) -> int:
        return abs(month1 - month2)

if __name__ == '__main__':
    calculator = MonthDifferenceCalculator()
    print(calculator.find_month_difference(5, 10))
    print(calculator.find_month_difference(12, 3))
    print(calculator.find_month_difference(7, 7))