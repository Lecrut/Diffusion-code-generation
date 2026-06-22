from datetime import date

def days_remaining_in_month(current_date):
    if not isinstance(current_date, date):
        raise ValueError('Input must be a date object')
    year = current_date.year
    month = current_date.month
    day = current_date.day
    if month == 12:
        last_day_of_month = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day_of_month = date(year, month + 1, 1) - timedelta(days=1)
    days_remaining = (last_day_of_month - current_date).days
    return days_remaining
if __name__ == '__main__':
    sample_date = date(2023, 4, 15)
    print(days_remaining_in_month(sample_date))