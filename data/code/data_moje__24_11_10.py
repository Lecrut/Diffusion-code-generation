def is_leap_year_bitwise(year):
    if year < 1:
        return False
    if (year & 3) != 0:
        return False
    if (year & 15) == 0:
        if (year % 400) == 0:
            return True
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        1,
        4,
        100,
        400,
        2000,
        1900,
        2004,
        2100,
        2400,
        1600,
        1700,
        1800,
        1996,
        1997,
        2003,
        2004,
        2005
    ]

    for year in test_cases:
        result = is_leap_year_bitwise(year)
        print(f"{year}: {result}")