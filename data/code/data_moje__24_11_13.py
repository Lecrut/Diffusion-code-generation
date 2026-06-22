def is_leap_year_year(n):
    if n & 3 != 0:
        return False
    if n & 15 != 0:
        return True
    return (n & 255) != 0 and (n & 511) == 0

def is_leap_year_optimized(n):
    if n % 4 != 0:
        return False
    if n % 100 != 0:
        return True
    return n % 400 == 0

def run_tests():
    assert is_leap_year_optimized(2000) == True
    assert is_leap_year_optimized(1900) == False
    assert is_leap_year_optimized(2004) == True
    assert is_leap_year_optimized(2001) == False
    assert is_leap_year_optimized(2400) == True
    assert is_leap_year_optimized(1800) == False
    assert is_leap_year_optimized(1600) == True
    assert is_leap_year_optimized(1700) == False
    assert is_leap_year_optimized(1200) == True
    assert is_leap_year_optimized(1100) == False

def check_leap_with_bitwise(n):
    is_div_by_4 = (n & 3) == 0
    if not is_div_by_4:
        return False
    is_div_by_100 = (n % 100) == 0
    if not is_div_by_100:
        return True
    return (n & 3) == 0 and (n & 255) == 0 and (n & 511) != 0

if __name__ == '__main__':
    run_tests()
    test_years = [2000, 1900, 2024, 2023, 1800, 2400, 2100, 2028, 1996, 1900]
    for year in test_years:
        print(year, check_leap_with_bitwise(year))