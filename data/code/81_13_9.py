from datetime import datetime, timedelta

SECONDS_PER_HOUR = 3600

def calculate_duration(start_time: str, end_time: str) -> float:
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    duration = end - start
    return duration.total_seconds() / SECONDS_PER_HOUR

if __name__ == '__main__':
    sample_start = "2023-10-01 12:00:00"
    sample_end = "2023-10-01 14:30:00"
    print(calculate_duration(sample_start, sample_end))