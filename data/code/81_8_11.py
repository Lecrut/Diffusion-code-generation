from datetime import datetime, timedelta

def calculate_elapsed_time(start_time, end_time):
    if start_time.tzinfo is None or end_time.tzinfo is None:
        raise ValueError("Both times must be timezone-aware")
    elapsed_time = end_time - start_time
    return elapsed_time.total_seconds() / 3600

if __name__ == '__main__':
    start_time = datetime(2023, 10, 1, 12, 0, 0, tzinfo=None)
    end_time = datetime(2023, 10, 1, 14, 30, 0, tzinfo=None)
    print(calculate_elapsed_time(start_time, end_time))