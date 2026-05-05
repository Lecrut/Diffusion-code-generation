import math
def time_difference_hours(timestamp1, timestamp2):
    difference_seconds = abs(timestamp1 - timestamp2)
    difference_hours = difference_seconds / 3600.0
    return difference_hours
if __name__ == '__main__':
    time1 = 1678886400.0
    time2 = 1678972800.0
    result = time_difference_hours(time1, time2)
    print(result)