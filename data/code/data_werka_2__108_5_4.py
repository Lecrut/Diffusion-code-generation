from datetime import datetime

def get_day_of_month(dt: datetime) -> int:
    epoch = datetime(1900, 1, 1)
    delta = dt - epoch
    total_days = delta.days
    year = dt.year
    base_days_for_years = (year - 1900) * 365
    leap_count = 0
    current_year = 1900
    while current_year < year:
        if current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0):
            leap_count += 1
        current_year += 1
    adjusted_days = total_days - base_days_for_years - leap_count
    days_in_months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_months[2] = 29
    month_idx = 0
    remaining = adjusted_days
    while remaining >= days_in_months[month_idx]:
        remaining -= days_in_months[month_idx]
        month_idx += 1
    day_of_month = remaining + 1
    return day_of_month

if __name__ == '__main__':
    sample_date = datetime(1999, 7, 23)
    result = get_day_of_month(sample_date)
    print(result)