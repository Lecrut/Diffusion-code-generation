def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) and ((year % 100 != 0) or (year % 4 == 0))
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024]
    for year in sample_years:
        print(f"{year}: {is_leap_year(year)}")