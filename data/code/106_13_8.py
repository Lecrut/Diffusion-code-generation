import time

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    if timestamp1 < 0 or timestamp2 < 0:
        raise ValueError("Timestamps must be non-negative")
    year1 = time.gmtime(timestamp1).tm_year
    year2 = time.gmtime(timestamp2).tm_year
    return abs(year1 - year2)

if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)