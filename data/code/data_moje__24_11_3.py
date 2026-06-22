def is_leap_year(year: int) -> bool:
    is_div_4 = (year & 3) == 0
    is_div_100 = (year & 3) == 0 if (year % 100) == 0 else False
    is_div_400 = (year & 3) == 0 if (year % 400) == 0 else False
    
    if is_div_400:
        return True
    if is_div_100:
        return False
    if is_div_4:
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        (2000, True),
        (1900, False),
        (2004, True),
        (2003, False),
        (4, True),
        (100, False),
        (400, True),
        (1600, True),
        (1700, False),
        (1800, False),
        (1900, False),
        (2000, True),
        (2004, True),
        (2008, True),
        (2020, True),
        (2023, False),
        (2100, False),
        (2400, True),
        (0, True),
        (40000, True),
        (200, False),
        (600, False),
        (800, False),
        (900, False),
        (1000, False),
        (1200, True),
        (1800, False),
        (1900, False),
        (2000, True),
        (2100, False),
        (2200, False),
        (2300, False),
        (2400, True),
        (2500, False),
        (2600, False),
        (2700, False),
        (2800, True),
        (-4, True),
        (-100, False),
        (-400, True),
    ]
    
    for year, expected in test_cases:
        result = is_leap_year(year)
        assert result == expected, f"Failed for year {year}: expected {expected}, got {result}"
        
    sample_years = [2000, 1900, 2004, 2003, 4]
    for y in sample_years:
        print(f"{y}: {is_leap_year(y)}")