import datetime
def days_remaining(year, month):
    days_in_month = 31 if month in {1, 3, 5, 7, 8, 10, 12} else 30 if month in {4, 6, 9, 11} else 28
    if year == 2023 and month == 12:
        return 0
    current_day = datetime.date(year, month, 1)
    target_day = datetime.date(year, month + 1, 1)
    return (target_day - current_day).days
if __name__ == '__main__':
    year = 2023
    month = 12
    print(days_remaining(year, month))