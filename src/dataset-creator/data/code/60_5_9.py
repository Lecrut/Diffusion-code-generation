def is_leap_year(year: int) -> bool:
    is_divisible_by_100 = (year % 100 == 0)
    is_divisible_by_4 = (year % 4 == 0)
    if not is_divisible_by_100:
        return is_divisible_by_4
    else:
        return is_divisible_by_4 and (year % 400 == 0)
if __name__ == '__main__':
    test_years = [2000, 1900, 2004, 2100, 2024]
    print("Leap Year Analysis:\n")
    for year in test_years:
        result = is_leap_year(year)
        if result:
            status_str = "LEAP YEAR"
        else:
            status_str = "COMMON YEAR"
        print(f"{year}: {status_str}")