def is_leap_year(year):
    return (year & 3 == 0) and ((year % 100 != 0) or (year % 400 == 0))

if __name__ == '__main__':
    years_to_check = [2000, 1900, 2024, 2023, 2400, 1600, 1700, 2004]
    results = {year: is_leap_year(year) for year in years_to_check}
    print(results)