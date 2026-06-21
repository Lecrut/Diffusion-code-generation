def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def test_static_assertions():
    assert is_leap_year(400) == True
    assert is_leap_year(100) == False
    assert is_leap_year(2000) == True

if __name__ == '__main__':
    test_static_assertions()
    print(is_leap_year(2024))
    print(is_leap_year(1900))
    print(is_leap_year(2000))