from datetime import datetime, timedelta

def remaining_hours_in_month(date):
    year = date.year
    month = date.month
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    last_day_of_current_month = datetime(year, month, 1) + timedelta(days=31)
    first_day_of_next_month = datetime(next_month[0], next_month[1], 1)
    remaining_days = (first_day_of_next_month - last_day_of_current_month).days
    return remaining_days * 24
if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    print(remaining_hours_in_month(sample_date))