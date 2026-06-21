import calendar

def is_leap_year(year):
    if not isinstance(year, int) or isinstance(year, bool):
        raise ValueError("Year must be an integer")
    if year < 1:
        raise ValueError("Year must be positive")
    return calendar.isleap(year)

if __name__ == '__main__':
    test_cases = [2000, 1900, 2024]
    for y in test_cases:
        print(is_leap_year(y))