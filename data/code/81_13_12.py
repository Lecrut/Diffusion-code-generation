from datetime import datetime

def calculate_duration_in_hours(start_timestamp, end_timestamp):
    start = datetime.fromisoformat(start_timestamp)
    end = datetime.fromisoformat(end_timestamp)
    duration = end - start
    return duration.total_seconds() / 3600.0

if __name__ == '__main__':
    sample_start = '2023-10-01T12:00:00'
    sample_end = '2023-10-01T14:30:00'
    print(calculate_duration_in_hours(sample_start, sample_end))