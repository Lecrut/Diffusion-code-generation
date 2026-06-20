from datetime import datetime

def calculate_time_difference(start_time, end_time):
    if start_time.tzinfo and end_time.tzinfo:
        time_difference = end_time - start_time
    else:
        raise ValueError("Both times must be timezone-aware")
    
    return time_difference.total_seconds() / 3600

if __name__ == '__main__':
    start_dt = datetime(2023, 10, 1, 12, 0, tzinfo=None)
    end_dt = datetime(2023, 10, 1, 14, 30, tzinfo=None)
    
    difference_in_hours = calculate_time_difference(start_dt, end_dt)
    print(f"Total elapsed time in hours: {difference_in_hours}")