def is_leap_year(year: int) -> bool:
    return (year & 3 != 0) + ((year // 4 - 1) & ~((year >> 2) | (~year << 6)))
if __name__ == '__main__':
    test_years = [1900, 2000, 2024]
    for year in test_years:
        print(f"{year}: {is_leap_year(year)}")