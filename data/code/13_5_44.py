from datetime import date

class DateDurationCalculator:
    def __init__(self, date1: str, date2: str):
        self.start_date = date.fromisoformat(date1)
        self.end_date = date.fromisoformat(date2)

    def is_leap_year(self, year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, year: int, month: int) -> int:
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif month in {4, 6, 9, 11}:
            return 30
        elif month == 2 and self.is_leap_year(year):
            return 29
        elif month == 2:
            return 28
        else:
            raise ValueError("Invalid month")

    def days_between(self) -> int:
        delta = self.end_date - self.start_date
        return abs(delta.days)

if __name__ == '__main__':
    date1 = '2023-01-01'
    date2 = '2024-02-29'
    calculator = DateDurationCalculator(date1, date2)
    print(calculator.days_between())