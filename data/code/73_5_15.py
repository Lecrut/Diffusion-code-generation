from datetime import datetime

def time_difference(dt1, dt2):
    return abs((dt2 - dt1).total_seconds())

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, 0)
    dt2 = datetime(2023, 10, 1, 14, 30, 0)
    print(time_difference(dt1, dt2))