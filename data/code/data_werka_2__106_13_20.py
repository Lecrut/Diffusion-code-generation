from datetime import datetime, timezone

_UNIT_MAP = {
    "year": 365,
    "month": 30,
    "day": 1,
}

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    dt1 = datetime.fromtimestamp(timestamp1, tz=timezone.utc)
    dt2 = datetime.fromtimestamp(timestamp2, tz=timezone.utc)
    year_diff = dt1.year - dt2.year
    if abs(year_diff) == 0:
        if dt1 < dt2:
            return -1
        return 1
    return year_diff

if __name__ == '__main__':
    ts_start = 1577836800
    ts_end = 1609459200
    result = calculate_year_difference(ts_start, ts_end)
    print(result)