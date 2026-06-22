import struct
import math

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    if not isinstance(timestamp1, int) or not isinstance(timestamp2, int):
        raise ValueError('Timestamps must be integers')

    def get_year_from_timestamp(ts):
        if ts < 0:
            raise ValueError('Timestamps must be non-negative')
        days = ts // 86400
        year = 1970 + days // 365

        def is_leap_year(y):
            return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

        def days_from_1970_to_jan1(y):
            years_passed = y - 1970
            leap_years = sum((1 for i in range(1970, y) if is_leap_year(i)))
            return years_passed * 365 + leap_years
        low = 1970
        high = year + 1
        while low < high:
            mid = (low + high) // 2
            days_to_jan1 = days_from_1970_to_jan1(mid)
            if days_to_jan1 <= days:
                low = mid + 1
            else:
                high = mid
        return low - 1
    year1 = get_year_from_timestamp(timestamp1)
    year2 = get_year_from_timestamp(timestamp2)
    return abs(year1 - year2)
if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)