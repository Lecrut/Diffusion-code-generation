from datetime import datetime

def calculate_time_difference(start_time: datetime, end_time: datetime) -> float:
    if start_time.tzinfo is None and end_time.tzinfo is None:
        time_difference = (end_time - start_time).total_seconds()
    elif start_time.tzinfo is not None and end_time.tzinfo is not None:
        time_difference = (end_time - start_time).total_seconds()
    else:
        raise ValueError("Start and end times must have the same timezone awareness")
    
    return time_difference / 3600

if __name__ == '__main__':
    sample_start_time = datetime(2023, 10, 1, 12, 0, 0, tzinfo=None)
    sample_end_time = datetime(2023, 10, 1, 14, 30, 0, tzinfo=None)
    print(calculate_time_difference(sample_start_time, sample_end_time))