def is_leap_year(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year < 0:
        raise ValueError("Year must be non-negative")
    if (year & 3) != 0:
        return False
    if (year % 100) != 0:
        return True
    if (year % 400) != 0:
        return False
    return True

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2400, 2100, 2004, 1999]
    for y in test_years:
        result = is_leap_year(y)
        print(f"{y}: {result}")