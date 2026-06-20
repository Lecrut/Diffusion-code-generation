import datetime

def calculate_duration_in_hours(start_time, end_time):
    duration = end_time - start_time
    return duration.total_seconds() / 3600

if __name__ == '__main__':
    start = datetime.datetime(2023, 10, 1, 12, 0)
    end = datetime.datetime(2023, 10, 1, 14, 30)
    print(calculate_duration_in_hours(start, end))