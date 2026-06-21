from datetime import datetime, timedelta

_DAYS_IN_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

_LEAP_DAYS = {1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096}

def days_in_month(year: int, month: int) -> int:
    if month not in _DAYS_IN_MONTH:
        raise ValueError("Invalid month")
    if month == 2 and year in _LEAP_DAYS:
        return 29
    return _DAYS_IN_MONTH[month]

def fraction_of_month_remaining(reference_date: datetime) -> float:
    year = reference_date.year
    month = reference_date.month
    day = reference_date.day
    hour = reference_date.hour
    minute = reference_date.minute
    second = reference_date.second
    microsecond = reference_date.microsecond
    
    total_days = days_in_month(year, month)
    
    current_day_fraction = (hour * 3600 + minute * 60 + second + microsecond / 1_000_000) / 86400.0
    current_day_absolute = day - 1 + current_day_fraction
    
    remaining_days = total_days - current_day_absolute
    
    if remaining_days <= 0:
        return 0.0
    if remaining_days >= total_days:
        return 1.0
        
    return remaining_days / total_days

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15, 12, 0, 0)
    result = fraction_of_month_remaining(sample_date)
    print(result)