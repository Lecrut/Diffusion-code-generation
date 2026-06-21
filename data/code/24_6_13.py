def is_leap_year(year):
    leap = (year & 3 == 0) and ((year % 100 != 0) or (year & 15 == 0 and year % 16 == 0))
    return leap

if __name__ == '__main__':
    years = [2000, 1900, 2004, 2023, 2400, 1600, 1700, 2024, 2025, 1200]
    results = {year: is_leap_year(year) for year in years}
    for year, is_leap in results.items():
        print(f"{year}: {is_leap}")