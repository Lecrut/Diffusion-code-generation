import datetime

class DateCalculator:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def get_next_day(cls, date_str: str) -> datetime.datetime:
        parts = date_str.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        
        if month < 1 or month > 12:
            raise ValueError(f"Invalid month: {month}")
        
        days_in_month = cls.MONTH_DAYS[month]
        if month == 2 and cls.is_leap_year(year):
            days_in_month += 1
        
        if day < 1 or day > days_in_month:
            raise ValueError(f"Invalid day {day} for month {month} in year {year}")
        
        day += 1
        if day > days_in_month:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        
        return datetime.datetime(year, month, day)

if __name__ == '__main__':
    input_date = '2000-02-28'
    result = DateCalculator.get_next_day(input_date)
    print(result)