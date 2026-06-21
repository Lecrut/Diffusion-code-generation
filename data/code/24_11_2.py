def is_leap_year(year):
    return (year & 3) == 0 and ((year % 100 != 0) or (year & 15) == 0 and (year & 240) == 0)

if __name__ == '__main__':
    test_cases = [
        (2000, True),
        (1900, False),
        (2004, True),
        (2001, False),
        (400, True),
        (100, False),
        (1, False),
        (0, True),
        (1700, False),
        (2400, True)
    ]

    for year, expected in test_cases:
        result = is_leap_year(year)
        assert result == expected
        print(f"{year}: {result}")