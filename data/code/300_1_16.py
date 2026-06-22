import calendar

class MonthDaysCalculator:
    def days_in_month(self, month: int, year: int) -> int:
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        return calendar.monthrange(year, month)[1]

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    print(calculator.days_in_month(1, 2023))
    print(calculator.days_in_month(12, 2024))
    print(calculator.days_in_month(2, 2024))
    print(calculator.days_in_month(7, 2025))