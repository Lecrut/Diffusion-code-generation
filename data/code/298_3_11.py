from datetime import time

def calculate_midnight_difference(time1, time2):
    if time1 > time2:
        midnight = time(0, 0)
        diff1 = time_diff(time1, midnight)
        diff2 = time_diff(midnight, time2)
        return (diff1 + diff2).total_seconds() / 3600
    else:
        return time_diff(time1, time2).total_seconds() / 3600

def time_diff(t1, t2):
    return abs((t2.hour - t1.hour) * 3600 + (t2.minute - t1.minute) * 60 + t2.second - t1.second)

if __name__ == '__main__':
    t1 = time(23, 59)
    t2 = time(0, 1)
    difference = calculate_midnight_difference(t1, t2)
    print(difference)