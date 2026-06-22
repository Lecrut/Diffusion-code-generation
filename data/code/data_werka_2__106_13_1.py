import datetime

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    dt1 = datetime.datetime.fromtimestamp(timestamp1)
    dt2 = datetime.datetime.fromtimestamp(timestamp2)
    return abs(dt1.year - dt2.year)

if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)