import datetime
if __name__ == '__main__':
    today = datetime.date(2023, 10, 15)
    year = today.year
    month = today.month
    if month == 12:
        days_in_month = 31
    else:
        days_in_month = 30 if (year % 4 != 0 or year % 100 != 0) else 31
    days_remaining = days_in_month - today.day
    print(days_remaining)