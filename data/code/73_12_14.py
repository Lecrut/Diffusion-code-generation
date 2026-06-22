import datetime

def calculate_time_difference_seconds(timestamp1: str, timestamp2: str) -> int:
    fmt = "%Y-%m-%dT%H:%M:%S"
    dt1 = datetime.datetime.strptime(timestamp1, fmt)
    dt2 = datetime.datetime.strptime(timestamp2, fmt)
    delta = dt2 - dt1
    return int(delta.total_seconds())

if __name__ == '__main__':
    ts1 = "2023-01-01T00:00:00"
    ts2 = "2023-01-02T12:30:00"
    result = calculate_time_difference_seconds(ts1, ts2)
    print(result)