from datetime import datetime

def calculate_time_difference(start_time: datetime, end_time: datetime) -> float:
    if start_time.tzinfo and end_time.tzinfo:
        difference = (end_time - start_time).total_seconds() / 3600
    else:
        raise ValueError("Both times must be timezone-aware")
    return difference

if __name__ == '__main__':
    sample_start_time = datetime(2023, 10, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    sample_end_time = datetime(2023, 10, 1, 14, 30, 0, tzinfo=datetime.timezone.utc)
    print(calculate_time_difference(sample_start_time, sample_end_time))