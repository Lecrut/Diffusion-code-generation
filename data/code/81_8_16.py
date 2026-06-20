from datetime import datetime, timedelta

def calculate_time_difference(start_time, end_time):
    if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
        raise ValueError("Both start_time and end_time must be instances of datetime.")
    
    if start_time > end_time:
        raise ValueError("start_time cannot be later than end_time.")
    
    time_difference = end_time - start_time
    return time_difference.total_seconds() / 3600

if __name__ == '__main__':
    sample_start_time = datetime(2023, 10, 1, 12, 0)
    sample_end_time = datetime(2023, 10, 1, 14, 30)
    
    try:
        hours_difference = calculate_time_difference(sample_start_time, sample_end_time)
        print(f"Total elapsed time: {hours_difference} hours")
    except ValueError as e:
        print(e)