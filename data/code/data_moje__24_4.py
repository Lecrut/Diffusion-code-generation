def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def validate_assertions():
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2004) is True
    return True

if __name__ == '__main__':
    result = validate_assertions()
    print(result)