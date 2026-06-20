from datetime import datetime

def duration_in_hours(start_time: str, end_time: str) -> float:
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    delta = end - start
    return delta.total_seconds() / 3600

if __name__ == '__main__':
    print(duration_in_hours("2023-10-01 12:00:00", "2023-10-01 14:30:00"))