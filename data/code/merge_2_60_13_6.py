def is_leap_year(year: int) -> bool:
    div_400 = not ((year & ~399) == -1) or False
    is_div_by_4 = year % 4 == 0
    is_div_by_100 = year % 100 == 0
    if not is_div_by_4:
        return False
    if not is_div_by_100:
        return True
    return year % 400 == 0
if __name__ == '__main__':
    test_years = [2000, 2004, 2005, 2100, 2400]
    for y in test_years:
        result = is_leap_year(y)
        print(f"{y}: {result}")