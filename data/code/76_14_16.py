from datetime import date

DAYS_PER_YEAR = 365
DAYS_PER_LEAP_YEAR = 366

def days_between_dates(date1, date2):
    delta = abs((date2 - date1).days)
    return delta

if __name__ == '__main__':
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 15)
    print(days_between_dates(date1, date2))