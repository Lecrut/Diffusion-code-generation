from datetime import datetime
def calculate_duration(dt1, dt2):
    return dt2 - dt1
if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 3, 14, 30, 0)
    duration = calculate_duration(time1, time2)
    print(duration)