from datetime import datetime

def calculate_elapsed_hours(start_time, end_time):
    return (end_time - start_time).total_seconds() / 3600.0

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 12, 0)
    end = datetime(2023, 1, 1, 14, 30)
    print(calculate_elapsed_hours(start, end))