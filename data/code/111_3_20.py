from datetime import date
import calendar

class DateArithmetic:
    def __init__(self, target_date: date):
        self.target_date = target_date

    def subtract_months(self, months: int) -> date:
        year = self.target_date.year
        month = self.target_date.month
        day = self.target_date.day

        total_months = year * 12 + (month - 1) - months
        new_year = total_months // 12
        new_month = total_months % 12 + 1

        max_day = calendar.monthrange(new_year, new_month)[1]
        new_day = min(day, max_day)

        return date(new_year, new_month, new_day)

    def add_months(self, months: int) -> date:
        return self.subtract_months(-months)

if __name__ == '__main__':
    start_date = date(2023, 10, 15)
    calculator = DateArithmetic(start_date)
    result = calculator.subtract_months(3)
    print(result)
    reversed_result = calculator.add_months(3)
    print(reversed_result)