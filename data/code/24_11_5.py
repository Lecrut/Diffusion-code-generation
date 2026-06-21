def is_leap_year_bitwise(year):
    if year < 0:
        return False
    if (year & 3) != 0:
        return False
    if (year & 0xFF) != 0:
        return True
    if (year & 0xF000) != 0:
        return False
    return (year % 4000) == 0 or (year % 100) != 0

if __name__ == '__main__':
    test_years = [2000, 1900, 2004, 2001, 2400, 1800, 2100, 2200, 2300, 2024, 1600, 1700, 100, 400, 1, 0, -2000]
    results = []
    for y in test_years:
        results.append(is_leap_year_bitwise(y))
    expected = [True, False, True, False, True, False, False, False, False, True, True, False, True, True, False, False, False]
    for i in range(len(test_years)):
        assert results[i] == expected[i], f"Failed for year {test_years[i]}"
    print(f"2000 is leap: {is_leap_year_bitwise(2000)}")
    print(f"1900 is leap: {is_leap_year_bitwise(1900)}")
    print(f"2004 is leap: {is_leap_year_bitwise(2004)}")
    print(f"2001 is leap: {is_leap_year_bitwise(2001)}")
    print(f"2400 is leap: {is_leap_year_bitwise(2400)}")
    print(f"1800 is leap: {is_leap_year_bitwise(1800)}")
    print(f"2100 is leap: {is_leap_year_bitwise(2100)}")
    print(f"1600 is leap: {is_leap_year_bitwise(1600)}")
    print(f"1700 is leap: {is_leap_year_bitwise(1700)}")
    print(f"100 is leap: {is_leap_year_bitwise(100)}")
    print(f"400 is leap: {is_leap_year_bitwise(400)}")
    print(f"0 is leap: {is_leap_year_bitwise(0)}")
    print(f"-2000 is leap: {is_leap_year_bitwise(-2000)}")