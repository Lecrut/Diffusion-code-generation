from calendar import isleap

def is_leap_year(year: int) -> bool:
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    return isleap(year)

if __name__ == '__main__':
    sample_years = (2000, 1900, 2024, 2023, 1600, 1700, 2400, 2100)
    results = [is_leap_year(y) for y in sample_years]
    for year, is_leap in zip(sample_years, results):
        print(is_leap)