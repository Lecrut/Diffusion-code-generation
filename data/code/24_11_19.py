def is_leap_year(year):
    return (year & 3 == 0) and ((year & 15 != 0) or (year % 400 == 0))

def test_leap_year():
    assert is_leap_year(4) == True
    assert is_leap_year(100) == False
    assert is_leap_year(400) == True
    assert is_leap_year(2000) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2024) == True
    assert is_leap_year(2023) == False
    assert is_leap_year(0) == True
    assert is_leap_year(-4) == True
    assert is_leap_year(-100) == False
    assert is_leap_year(-400) == True

if __name__ == '__main__':
    test_leap_year()
    print(is_leap_year(2024))
    print(is_leap_year(1900))
    print(is_leap_year(2000))
    print(is_leap_year(2023))
    print(is_leap_year(4))
    print(is_leap_year(100))