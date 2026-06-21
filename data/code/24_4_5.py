def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

assert is_leap_year(2000) == True, "2000 is a leap year"
assert is_leap_year(1900) == False, "1900 is not a leap year"
assert is_leap_year(2004) == True, "2004 is a leap year"

if __name__ == '__main__':
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(2000))