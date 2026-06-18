def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    sample_years = [2023, 2024, 1900, 2000]
    for y in sample_years:
        print(f"{y}: {is_leap_year(y)}")