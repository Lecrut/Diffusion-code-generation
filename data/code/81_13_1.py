from datetime import datetime, timedelta

def calculate_duration(start_time: str, end_time: str) -> float:
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    duration = end - start
    return duration.total_seconds() / 3600

if __name__ == '__main__':
    start = "2023-10-01 12:00:00"
    end = "2023-10-01 14:30:00"
    print(calculate_duration(start, end))