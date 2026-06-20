import datetime

def time_difference_in_hours(dt1, dt2):
    difference = abs(dt1 - dt2)
    hours = difference.total_seconds() / 3600.0
    return hours

if __name__ == '__main__':
    dt1 = datetime.datetime(2023, 3, 1, 0, 0, 0)
    dt2 = datetime.datetime(2023, 3, 1, 3, 30, 0)
    result = time_difference_in_hours(dt1, dt2)
    print(result)