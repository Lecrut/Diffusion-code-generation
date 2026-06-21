import time

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    date1 = time.gmtime(timestamp1)
    date2 = time.gmtime(timestamp2)
    return abs(date1.tm_year - date2.tm_year)

if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)