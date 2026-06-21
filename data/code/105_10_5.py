from datetime import datetime

class DateCalculator:
    DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    @staticmethod
    def _is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_days_in_month(year: int, month: int) -> int:
        if month == 2:
            return 29 if DateCalculator._is_leap_year(year) else 28
        return DateCalculator.DAYS_IN_MONTH[month]

    @staticmethod
    def get_next_day(date_str: str) -> datetime:
        parts = date_str.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        
        max_day = DateCalculator.get_days_in_month(year, month)
        
        if day < max_day:
            day += 1
        else:
            day = 1
            if month < 12:
                month += 1
            else:
                month = 1
                year += 1
        
        return datetime(year, month, day)

if __name__ == '__main__':
    sample_date = '2024-02-28'
    result = DateCalculator.get_next_day(sample_date)
    print(result)