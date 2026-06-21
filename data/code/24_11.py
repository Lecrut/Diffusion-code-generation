def is_leap_year(year: int) -> bool:
    if year & 3:
        return False
    if year % 100:
        return True
    if year & 31:
        return False
    return True

if __name__ == '__main__':
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False
    assert is_leap_year(1600) is True
    assert is_leap_year(1700) is False
    assert is_leap_year(1800) is False
    assert is_leap_year(2400) is True
    assert is_leap_year(2100) is False
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(1600))
    print(is_leap_year(1700))
    print(is_leap_year(1800))
    print(is_leap_year(2400))
    print(is_leap_year(2100))