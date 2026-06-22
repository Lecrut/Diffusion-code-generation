from datetime import datetime

def calculate_time_difference_seconds(timestamp1: str, timestamp2: str) -> float:
    fmt = "%Y-%m-%dT%H:%M:%S"
    dt1 = datetime.strptime(timestamp1, fmt)
    dt2 = datetime.strptime(timestamp2, fmt)
    delta = dt2 - dt1
    return delta.total_seconds()

if __name__ == '__main__':
    ts1 = "2023-10-01T12:00:00"
    ts2 = "2023-10-01T12:01:30"
    result = calculate_time_difference_seconds(ts1, ts2)
    print(result)