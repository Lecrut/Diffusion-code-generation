import datetime
def days_remaining(year, month):
    days_in_month = 31 if month in {1, 3, 5, 7, 8, 10, 12} else 30 if month in {4, 6, 9, 11} else 28
    days_in_year = 366 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 365
    if month == 12:
        return 0
    else:
        return (days_in_month - (datetime.date(year, month + 1, 1).day - 1))
if __name__ == '__main__':
    year = 2023
    month = 12
    print(days_remaining(year, month))