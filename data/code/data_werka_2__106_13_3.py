from calendar import timegm
from datetime import datetime, timezone

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    dt1 = datetime.fromtimestamp(timestamp1, tz=timezone.utc)
    dt2 = datetime.fromtimestamp(timestamp2, tz=timezone.utc)
    return abs(dt1.year - dt2.year)

if __name__ == '__main__':
    ts1 = 1577836800
    ts2 = 1609459200
    result = calculate_year_difference(ts1, ts2)
    print(result)