from datetime import datetime, timedelta

def days_remaining_in_month():
    today = datetime.now()
    _, last_day_of_month = calendar.monthrange(today.year, today.month)
    last_date_of_month = datetime(today.year, today.month, last_day_of_month)
    return (last_date_of_month - today).days

if __name__ == '__main__':
    print(days_remaining_in_month())