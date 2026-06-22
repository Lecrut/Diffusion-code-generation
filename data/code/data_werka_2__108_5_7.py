from datetime import datetime

DAYS_IN_COMMON_YEAR = 365
DAYS_IN_LEAP_YEAR = 366
DAYS_IN_MONTHS_COMMON = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
DAYS_IN_MONTHS_LEAP = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
YEAR_ZERO = 1
MONTH_ONE = 1
DAY_ONE = 1
LEAP_DIVISOR = 4
CENTURY_DIVISOR = 100
MILLENNIUM_DIVISOR = 400

def is_leap_year(year: int) -> bool:
    return (year % LEAP_DIVISOR == 0 and year % CENTURY_DIVISOR != 0) or (year % MILLENNIUM_DIVISOR == 0)

def get_day_of_month(dt: datetime) -> int:
    days_to_subtract = 0
    year = dt.year
    current_y = YEAR_ZERO
    while current_y < year:
        if is_leap_year(current_y):
            days_to_subtract += DAYS_IN_LEAP_YEAR
        else:
            days_to_subtract += DAYS_IN_COMMON_YEAR
        current_y += 1
    
    is_current_leap = is_leap_year(year)
    month_days = DAYS_IN_MONTHS_LEAP if is_current_leap else DAYS_IN_MONTHS_COMMON
    
    month = dt.month
    days_to_subtract += sum(month_days[:month])
    
    day = dt.day
    total_days_from_epoch = days_to_subtract + day
    
    if month == MONTH_ONE and day == DAY_ONE:
        return DAY_ONE
    
    days_in_current_month = month_days[month]
    
    if total_days_from_epoch <= 0:
        return -total_days_from_epoch
    
    return total_days_from_epoch % days_in_current_month if total_days_from_epoch > days_in_current_month else total_days_from_epoch

if __name__ == '__main__':
    sample_dt = datetime(2024, 2, 29)
    day_value = get_day_of_month(sample_dt)
    print(day_value)