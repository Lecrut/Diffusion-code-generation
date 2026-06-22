def is_leap_year(year):
    if year & 3:
        return False
    if year & 192 == 0:
        if year & 32767 == 0:
            return False
    return True

if __name__ == '__main__':
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2024) is True
    assert is_leap_year(2100) is False
    assert is_leap_year(4) is True
    assert is_leap_year(100) is False
    assert is_leap_year(400) is True
    assert is_leap_year(1) is False
    assert is_leap_year(2023) is False
    assert is_leap_year(2400) is True
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2100))
    print(is_leap_year(4))
    print(is_leap_year(100))
    print(is_leap_year(400))
    print(is_leap_year(1))
    print(is_leap_year(2023))
    print(is_leap_year(2400))