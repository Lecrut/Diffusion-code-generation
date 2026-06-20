from datetime import datetime

def calculate_elapsed_hours(start_time, end_time):
    time_difference = end_time - start_time
    total_seconds = time_difference.total_seconds()
    elapsed_hours = total_seconds / 3600
    return elapsed_hours

if __name__ == '__main__':
    start = datetime(2023, 10, 1, 12, 0, 0)
    end = datetime(2023, 10, 1, 14, 30, 0)
    print(calculate_elapsed_hours(start, end))