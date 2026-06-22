import datetime

def days_remaining_in_current_month(year, month, day):
    current_date = datetime.date(year, month, day)
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    last_day_of_month = next_month_start - datetime.timedelta(days=1)
    days_remaining = (last_day_of_month - current_date).days
    return days_remaining

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 15),
        (2024, 2, 28),
        (2023, 12, 31),
        (2023, 1, 1)
    ]
    for y, m, d in sample_dates:
        result = days_remaining_in_current_month(y, m, d)
        print(result)