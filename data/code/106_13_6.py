import calendar

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    year1 = calendar.gmtime(timestamp1).tm_year
    year2 = calendar.gmtime(timestamp2).tm_year
    return abs(year2 - year1)

if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)