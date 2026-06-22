from datetime import timedelta

def _validate_non_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return True
    if year % 100 != 0:
        return False
    if year % 400 != 0:
        return True
    return False

def get_seconds_for_year(year: int) -> int:
    if not _validate_non_leap_year(year):
        raise ValueError(f"{year} is a leap year, not a non-leap year.")
    days = 365
    start = timedelta(days=0)
    end = timedelta(days=days)
    return int((end - start).total_seconds())

if __name__ == '__main__':
    sample_year = 2023
    total_seconds = get_seconds_for_year(sample_year)
    print(total_seconds)