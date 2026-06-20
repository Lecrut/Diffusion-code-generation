import datetime

def calculate_remaining_days(current_date):
    current_year = current_date.year
    current_month = current_date.month
    next_month_start = datetime.date(current_year, current_month + 1, 1)
    if current_month == 12:
        next_month_start = datetime.date(current_year + 1, 1, 1)
    month_end = next_month_start - datetime.timedelta(days=1)
    days_remaining = (month_end - current_date).days
    return days_remaining

if __name__ == '__main__':
    current_date = datetime.date(2024, 6, 15)
    remaining_days = calculate_remaining_days(current_date)
    print(remaining_days)