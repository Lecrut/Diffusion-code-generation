import math
def time_difference_hours(timestamp1, timestamp2):
    difference = timestamp1 - timestamp2
    hours = difference / 3600.0
    return hours
if __name__ == '__main__':
    time1 = 1678886400.0
    time2 = 1678890000.0
    result = time_difference_hours(time1, time2)
    print(result)