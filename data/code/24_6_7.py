def is_leap_year(year: int) -> bool:
    if (year & 3) != 0:
        return False
    if (year % 100) != 0:
        return True
    return (year % 400) == 0

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2100, 2400]
    for y in test_years:
        print(f"{y}: {is_leap_year(y)}")