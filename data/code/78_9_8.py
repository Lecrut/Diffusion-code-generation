class MonthDifferenceCalculator:
    def calculate_difference(self, start_month: int, end_month: int) -> int:
        return abs(end_month - start_month)

if __name__ == '__main__':
    calculator = MonthDifferenceCalculator()
    print(calculator.calculate_difference(5, 10))
    print(calculator.calculate_difference(12, 2))
    print(calculator.calculate_difference(-3, -9))
    print(calculator.calculate_difference(-12, -2))