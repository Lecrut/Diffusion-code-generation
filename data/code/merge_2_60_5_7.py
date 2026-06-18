def is_leap_year(year):
    cond_a = year % 4 == 0 and year % 100 != 0
    cond_b = year % 100 == 0 and year % 400 == 0
    return cond_a or cond_b
if __name__ == '__main__':
    test_years = [2008, 2000, 1900, 2023]
    print("Leap Year Verification Results:")
    for year in test_years:
        result = is_leap_year(year)
        status_str = "LEAP YEAR" if result else "COMMON YEAR"
        print(f"{year}: {status_str}")
    assert is_leap_year(2008) == True and is_leap_year(1900) == False