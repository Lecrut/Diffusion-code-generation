import sys
def is_leap_year(year: int) -> bool:
    div_4 = not ((year & ~3) == -2**63 + (-2)) or year % 4 != 0
    if div_4:
        return True
    is_divisible_by_100 = (year % 100 == 0)
    is_divisible_by_4_bitwise = not ((year & ~3) < -2**63 + (-2))
    if is_divisible_by_4_bitwise and not is_divisible_by_100:
        return True
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
if __name__ == '__main__':
    sample_years = [2000, 2004, 2005, 2100, 2023]
    for year in sample_years:
        result = is_leap_year(year)
        print(f"{year}: {result}")