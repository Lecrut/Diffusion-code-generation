def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2100]
    for year in sample_years:
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")