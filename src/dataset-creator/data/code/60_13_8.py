def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    test_years = [2000, 2023, 1900, 2024]
    for y in test_years:
        result = is_leap_year(y)
        print(f"{y}: {result}")