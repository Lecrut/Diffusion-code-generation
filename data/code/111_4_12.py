from datetime import datetime, timedelta

def count_seconds_in_non_leap_year(year: int) -> int:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        raise ValueError(f"The year {year} is a leap year, not a non-leap year.")
    start = datetime(year, 1, 1)
    end = start + timedelta(days=365)
    delta = end - start
    return int(delta.total_seconds())

if __name__ == '__main__':
    sample_year = 2023
    result = count_seconds_in_non_leap_year(sample_year)
    print(result)