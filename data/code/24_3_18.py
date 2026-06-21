def is_leap_year(year: int) -> bool:
    if year < 0:
        raise ValueError("Year must be a positive integer")
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    test_years = [2000, 1900, 2004, 2001, 2400, 1800, 2024, 2023]
    for year in test_years:
        result = is_leap_year(year)
        print(f"{year}: {result}")