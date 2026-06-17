from datetime import datetime
def calculate_duration(start_time, end_time):
    return end_time - start_time
if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 1, 10, 30, 15)
    duration = calculate_duration(time1, time2)
    print(duration)