import datetime

def days_in_month(year, month):
    return calendar.monthrange(year, month)[1]

def calculate_remaining_days(date):
    today = date.today()
    year, month = today.year, today.month
    days_in_current_month = days_in_month(year, month)
    if today.day == 1:
        remaining_days = days_in_current_month - 1
    else:
        remaining_days = days_in_current_month - today.day
    return remaining_days

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    remaining = calculate_remaining_days(sample_date)
    print(remaining)