from datetime import datetime
import calendar

class DateCalculator:
    DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_max_days(month: int, year: int) -> int:
        if month == 2:
            return 29 if DateCalculator.is_leap_year(year) else 28
        return DateCalculator.DAYS_IN_MONTH[month]

    @staticmethod
    def calculate_next_day(date_str: str) -> datetime:
        parts = date_str.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        max_days = DateCalculator.get_max_days(month, year)

        if day < max_days:
            return datetime(year, month, day + 1)
        
        if month < 12:
            return datetime(year, month + 1, 1)
        
        return datetime(year + 1, 1, 1)

if __name__ == '__main__':
    input_date = '2024-02-28'
    calc = DateCalculator()
    next_date = calc.calculate_next_day(input_date)
    print(next_date)