def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    assert is_leap_year(2000) == True
    assert is_leap_year(2004) == True
    assert is_leap_year(1900) == False
    print(is_leap_year(2024))
    print(is_leap_year(2100))
    print(is_leap_year(2023))