def is_leap_year_bitwise(year):
    if year < 1:
        raise ValueError("Year must be positive")
    if (year & 3) != 0:
        return False
    if (year & 15) == 0:
        return (year % 400) == 0
    return True

if __name__ == '__main__':
    test_cases = [
        1, 4, 100, 400, 1700, 1800, 1900, 2000, 2001, 2004, 2100, 2400
    ]
    for year in test_cases:
        result = is_leap_year_bitwise(year)
        print(f"Year {year}: {result}")