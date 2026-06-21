def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

assert is_leap_year(2000) == True
assert is_leap_year(2400) == True
assert is_leap_year(1900) == False

if __name__ == '__main__':
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(2100))