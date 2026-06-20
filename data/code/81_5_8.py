from datetime import datetime

def calculate_duration_in_hours(start_time, end_time):
    time_difference = end_time - start_time
    return time_difference.total_seconds() / 3600

if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 3, 14, 30, 0)
    hours = calculate_duration_in_hours(time1, time2)
    print(hours)