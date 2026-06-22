from datetime import time, timedelta

def calculate_midnight_difference(time1, time2):
    if time1 < time2:
        return time2 - time1
    else:
        return timedelta(hours=24) + time2 - time1

if __name__ == '__main__':
    t1 = time(23, 59)
    t2 = time(0, 1)
    diff = calculate_midnight_difference(t1, t2)
    print(diff)