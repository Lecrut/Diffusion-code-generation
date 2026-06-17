import datetime
def days_remaining(year, month):
    if month == 12:
        return 31 - datetime.date(year, 12, 1).day
    else:
        days_in_month = 31 if month in {1, 3, 5, 7, 8, 10, 12} else 30
        return days_in_month - datetime.date(year, month, 1).day
if __name__ == '__main__':
    year = 2023
    month = 12
    print(days_remaining(year, month))