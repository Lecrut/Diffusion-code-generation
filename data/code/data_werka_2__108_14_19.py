import datetime

_DAYS_IN_MONTHS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

_LEAP_YEAR_THRESHOLD = 4
_CENTURY_THRESHOLD = 100
_MILLENNIUM_THRESHOLD = 400

def get_day_of_month(date_obj: datetime.date) -> int:
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be a datetime.date instance")
    return date_obj.day

def is_leap_year(year: int) -> bool:
    if year % _MILLENNIUM_THRESHOLD == 0:
        return year % _MILLENNIUM_THRESHOLD == 0
    if year % _CENTURY_THRESHOLD == 0:
        return False
    return year % _LEAP_YEAR_THRESHOLD == 0

def get_days_in_month(year: int, month: int) -> int:
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    days = _DAYS_IN_MONTHS[month]
    if month == 2 and is_leap_year(year):
        days += 1
    return days

if __name__ == '__main__':
    sample_date = datetime.date(2024, 2, 29)
    day_value = get_day_of_month(sample_date)
    print(day_value)
    
    days_in_feb = get_days_in_month(2024, 2)
    print(days_in_feb)
    
    days_in_jan = get_days_in_month(2023, 1)
    print(days_in_jan)