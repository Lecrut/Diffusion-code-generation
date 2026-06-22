from datetime import timedelta
import calendar

def calculate_seconds_in_year(year: int) -> int:
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")
    if calendar.isleap(year):
        raise ValueError("Year must not be a leap year")
    
    days_in_year = 365
    seconds_per_day = 86400
    return days_in_year * seconds_per_day

def get_seconds_for_non_leap_year(year: int) -> int:
    return calculate_seconds_in_year(year)

if __name__ == '__main__':
    sample_year = 2023
    result = get_seconds_for_non_leap_year(sample_year)
    print(result)