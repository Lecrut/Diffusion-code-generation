import struct

def get_year_from_timestamp(timestamp: int) -> int:
    if not isinstance(timestamp, int):
        raise ValueError('Timestamp must be an integer')
    if timestamp < 0:
        raise ValueError('Timestamp must be non-negative')
    days = timestamp // 86400
    y = 1970 + days // 365

    def days_before_year(yr):
        y0 = 1970
        return 365 * (yr - y0) + (yr - 1) // 4 - (yr - 1) // 100 + (yr - 1) // 400 - (y0 - 1) // 4 + (y0 - 1) // 100 - (y0 - 1) // 400
    y_days = days_before_year(y)
    if days < y_days:
        y -= 1
    else:
        y_next_days = days_before_year(y + 1)
        if days >= y_next_days:
            y += 1
    return y

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    year1 = get_year_from_timestamp(timestamp1)
    year2 = get_year_from_timestamp(timestamp2)
    return abs(year1 - year2)
if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)