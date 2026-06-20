import datetime

DAYS_PER_YEAR = 365.25
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def days_between(date1, date2):
    delta = abs(date2 - date1)
    return delta.days + delta.seconds / (SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY)

if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    d2 = datetime.datetime(2023, 10, 25, 15, 45, 0)
    d3 = datetime.datetime(2024, 1, 1, 0, 0, 0)
    d4 = datetime.datetime(2024, 1, 1, 0, 0, 0)
    print(days_between(d1, d2))
    print(days_between(d3, d4))
    print(days_between(d2, d1))
    print(days_between(d4, d3))
    print(days_between(d1, d1))