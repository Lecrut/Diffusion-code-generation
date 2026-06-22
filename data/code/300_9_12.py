from datetime import datetime, timedelta

def days_remaining_in_month():
    today = datetime.now()
    last_day_of_month = datetime(today.year, today.month + 1, 1) - timedelta(days=1)
    return (last_day_of_month - today).days

if __name__ == '__main__':
    print(days_remaining_in_month())