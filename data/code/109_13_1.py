import datetime
if __name__ == '__main__':
    today = datetime.date(2023, 10, 15)
    year = today.year
    month = today.month
    if month == 12:
        days_in_month = 31
        days_remaining = days_in_month - today.day
    else:
        days_in_month = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30
        days_remaining = days_in_month - today.day
    print(days_remaining)