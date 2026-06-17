import calendar
from datetime import date
def calculate_days_remaining(target_year, target_month):
    today = date.today()
    if target_month == 12:
        next_month_year = today.year + 1
        next_month = 1
    else:
        next_month_year = today.year
        next_month = target_month + 1
    try:
        first_day_of_next_month = date(next_month_year, next_month, 1)
    except ValueError:
        if target_month == 12:
            first_day_of_next_month = date(today.year + 1, 1, 1)
        else:
            first_day_of_next_month = date(today.year, target_month + 1, 1)
    days_in_target_month = calendar.monthrange(target_year, target_month)[1]
    days_remaining = days_in_target_month
    return days_remaining
if __name__ == '__main__':
    print(calculate_days_remaining(2023, 1))
    print(calculate_days_remaining(2023, 6))
    print(calculate_days_remaining(2024, 12))
    print(calculate_days_remaining(2025, 3))