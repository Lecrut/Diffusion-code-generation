from datetime import datetime

def calculate_time_elapsed():
    start = datetime(2023, 1, 1, 12, 0, 0)
    end = datetime(2023, 1, 2, 14, 30, 0)
    time_difference = end - start
    hours_elapsed = time_difference.total_seconds() / 3600
    return hours_elapsed

if __name__ == '__main__':
    print(calculate_time_elapsed())