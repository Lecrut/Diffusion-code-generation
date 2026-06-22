from datetime import date
import calendar

class DayOfMonthCalculator:
    def __init__(self, year: int, month: int, day: int) -> None:
        self._date = date(year, month, day)

    def get_day(self) -> int:
        return self._date.day

    def get_month(self) -> int:
        return self._date.month

    def get_year(self) -> int:
        return self._date.year

    def get_weekday_name(self) -> str:
        return self._date.strftime("%A")

    def is_leap_year(self) -> bool:
        return calendar.isleap(self._date.year)

if __name__ == '__main__':
    calc = DayOfMonthCalculator(2024, 10, 10)
    print(calc.get_day())
    print(calc.get_month())
    print(calc.get_year())
    print(calc.get_weekday_name())
    print(calc.is_leap_year())