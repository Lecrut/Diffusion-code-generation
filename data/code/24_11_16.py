def is_leap_year(year):
    not_divisible_by_4 = year & 3
    if not_divisible_by_4:
        return False
    if not (year & 0xFF00):
        return bool(year & 0x400)
    return True

if __name__ == '__main__':
    test_years = [1600, 1700, 1800, 1900, 2000, 2004, 2100, 2400, 1999, 2024]
    for y in test_years:
        print(is_leap_year(y))
    assert is_leap_year(1600) is True
    assert is_leap_year(1700) is False
    assert is_leap_year(1800) is False
    assert is_leap_year(1900) is False
    assert is_leap_year(2000) is True
    assert is_leap_year(2004) is True
    assert is_leap_year(2100) is False
    assert is_leap_year(2400) is True
    assert is_leap_year(1999) is False
    assert is_leap_year(2024) is True