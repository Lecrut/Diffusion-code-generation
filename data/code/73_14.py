import time
def time_difference_in_hours(timestamp1, timestamp2):
    difference = timestamp2 - timestamp1
    hours = difference / 3600.0
    return hours
if __name__ == '__main__':
    time1 = 1678886400.0
    time2 = 1678972800.0
    result = time_difference_in_hours(time1, time2)
    print(result)