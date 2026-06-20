import datetime

def calculate_remaining_minutes():
    today = datetime.date.today()
    year = today.year
    month = today.month
    last_day_of_month = (datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)).day
    remaining_days = last_day_of_month - today.day
    remaining_minutes = remaining_days * 24 * 60
    return remaining_minutes

if __name__ == '__main__':
    print(calculate_remaining_minutes())