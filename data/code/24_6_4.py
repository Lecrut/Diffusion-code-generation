def is_leap_year(year):
    return (year & 3 == 0) and ((year & 15 != 0) or (year % 400 == 0))

if __name__ == '__main__':
    sample_years = [2000, 1900, 2004, 2001, 2400, 1800, 2023, 2024]
    for year in sample_years:
        print(is_leap_year(year))