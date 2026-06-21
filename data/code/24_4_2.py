def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False

if __name__ == '__main__':
    assert is_leap_year(2000) is True
    assert is_leap_year(2004) is True
    assert is_leap_year(1900) is False
    print(is_leap_year(2024))