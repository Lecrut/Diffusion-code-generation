import datetime

HOURS_PER_DAY = 24
SECONDS_PER_HOUR = 3600

def time_difference_in_hours(datetime1, datetime2):
    difference = abs(datetime2 - datetime1)
    hours = (difference.days * HOURS_PER_DAY) + (difference.seconds / SECONDS_PER_HOUR)
    return hours

if __name__ == '__main__':
    dt1 = datetime.datetime(2023, 1, 1, 12, 0, 0)
    dt2 = datetime.datetime(2023, 1, 2, 14, 30, 0)
    result = time_difference_in_hours(dt1, dt2)
    print(result)