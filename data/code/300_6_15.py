from datetime import datetime

DAYS_IN_YEAR = 365

def days_remaining_in_month():
    today = datetime.now()
    year = today.year
    month = today.month
    last_day_of_month = (datetime(year, month + 1, 1) - timedelta(days=1)).day
    return last_day_of_month - today.day

if __name__ == '__main__':
    print(f"Days remaining in the current month: {days_remaining_in_month()}")