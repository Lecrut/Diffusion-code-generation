def is_leap_year(year):
    if year & 3 != 0:
        return False
    if year % 100 != 0:
        return True
    return year % 400 == 0

def run_assertions():
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2004) is True
    assert is_leap_year(2003) is False
    assert is_leap_year(1800) is False
    assert is_leap_year(1600) is True
    assert is_leap_year(2400) is True
    assert is_leap_year(2100) is False
    assert is_leap_year(1) is False
    assert is_leap_year(4) is True

if __name__ == '__main__':
    run_assertions()
    test_years = [1600, 1700, 1800, 1900, 2000, 2004, 2100, 2400]
    for year in test_years:
        print(year, is_leap_year(year))