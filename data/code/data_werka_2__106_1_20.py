from datetime import date

DAYS_IN_LEAP_YEAR = 366
DAYS_IN_COMMON_YEAR = 365
DATE_FORMAT = "%Y-%m-%d"

def _is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def _count_days_in_year(year):
    if _is_leap_year(year):
        return DAYS_IN_LEAP_YEAR
    return DAYS_IN_COMMON_YEAR

def _count_days_from_epoch_to_date(year, month, day):
    total_days = 0
    for y in range(1, year):
        total_days += _count_days_in_year(y)
    
    months_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if _is_leap_year(year):
        months_days[2] = 29
    
    for m in range(1, month):
        total_days += months_days[m]
    
    total_days += day
    return total_days

def calculate_integer_year_difference(date_str1, date_str2):
    d1 = date.fromisoformat(date_str1)
    d2 = date.fromisoformat(date_str2)
    
    days1 = _count_days_from_epoch_to_date(d1.year, d1.month, d1.day)
    days2 = _count_days_from_epoch_to_date(d2.year, d2.month, d2.day)
    
    diff_days = abs(days2 - days1)
    
    years = diff_days // 365
    return years

if __name__ == '__main__':
    result = calculate_integer_year_difference("2020-02-29", "2023-03-01")
    print(result)