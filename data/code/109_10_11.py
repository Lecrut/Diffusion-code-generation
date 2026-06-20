import datetime

def days_remaining_in_month():
    today = datetime.date.today()
    current_year, current_month = today.year, today.month
    last_day_of_current_month = datetime.date(current_year, current_month + 1, 1) - datetime.timedelta(days=1)
    return (last_day_of_current_month - today).days

if __name__ == '__main__':
    sample_days_left = days_remaining_in_month()
    print(sample_days_left)