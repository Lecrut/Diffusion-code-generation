from datetime import datetime

def duration_in_hours(start_time: str, end_time: str) -> float:
    time_format = "%Y-%m-%d %H:%M:%S"
    start_dt = datetime.strptime(start_time, time_format)
    end_dt = datetime.strptime(end_time, time_format)
    delta = end_dt - start_dt
    return delta.total_seconds() / 3600

if __name__ == '__main__':
    print(duration_in_hours("2023-10-01 12:00:00", "2023-10-01 14:30:00"))