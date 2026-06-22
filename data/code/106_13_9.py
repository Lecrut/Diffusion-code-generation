import struct
import math

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    if not isinstance(timestamp1, int) or not isinstance(timestamp2, int):
        raise ValueError("Timestamps must be integers")
    
    def get_year(ts):
        if ts < 0:
            raise ValueError("Timestamps must be non-negative")
        days = ts // 86400
        y = 1970
        while True:
            leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
            days_in_year = 366 if leap else 365
            if days < days_in_year:
                break
            days -= days_in_year
            y += 1
        return y
    
    year1 = get_year(timestamp1)
    year2 = get_year(timestamp2)
    return abs(year1 - year2)

if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)