import datetime
if __name__ == '__main__':
    month = 10
    year = 2023
    target_date = datetime.date(year, month, 1)
    if month == 12:
        days_left = 0
    else:
        target_end = datetime.date(year, month, 1) + datetime.timedelta(days=31)
        days_left = (target_end - datetime.date(year, month + 1, 1)).days
    print(f"Month: {month}, Year: {year}")
    print(f"Days left until the end of the month: {days_left}")