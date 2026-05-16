import math
def time_difference_hours(timestamp1, timestamp2):
    time_difference = abs(timestamp1 - timestamp2)
    hours = time_difference / 3600.0
    return hours
if __name__ == '__main__':
    time1 = 1678886400.0
    time2 = 1678972800.0
    difference = time_difference_hours(time1, time2)
    print(difference)