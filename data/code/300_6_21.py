import datetime

def days_remaining(month):
    today = datetime.date.today()
    last_day_of_month = datetime.date(today.year, month + 1, 1) - datetime.timedelta(days=1)
    return (last_day_of_month - today).days

if __name__ == '__main__':
    print(f"Days remaining in March 2024: {days_remaining(3)}")
    print(f"Days remaining in February 2023: {days_remaining(2)}")
    print(f"Days remaining in December 2024: {days_remaining(12)}")