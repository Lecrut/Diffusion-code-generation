import struct
import sys

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    if not isinstance(timestamp1, int) or not isinstance(timestamp2, int):
        raise ValueError('Timestamps must be integers')
    epoch_year = 1970
    days_per_400_years = 146097
    days_per_100_years = 36525
    days_per_4_years = 1461
    days_per_year = 365

    def _get_year_from_days(total_days):
        days_per_4_years_count, remainder = divmod(total_days, days_per_400_years)
        year = days_per_400_years_count * 400
        days_per_100_years_count, remainder = divmod(remainder, days_per_100_years)
        year += days_per_100_years_count * 100
        if days_per_100_years_count == 4:
            year -= 1
            remainder += days_per_100_years
        days_per_4_years_count, remainder = divmod(remainder, days_per_4_years)
        year += days_per_4_years_count * 4
        days_per_year_count, remainder = divmod(remainder, days_per_year)
        year += days_per_year_count
        year += 1
        return year
    seconds_per_day = 86400
    offset = timestamp1 // seconds_per_day
    total_days1 = offset
    if offset < 0 and timestamp1 % seconds_per_day != 0:
        total_days1 -= 1
    seconds_per_day = 86400
    offset2 = timestamp2 // seconds_per_day
    total_days2 = offset2
    if offset2 < 0 and timestamp2 % seconds_per_day != 0:
        total_days2 -= 1
    year1 = _get_year_from_days(total_days1)
    year2 = _get_year_from_days(total_days2)
    return abs(year1 - year2)
if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)