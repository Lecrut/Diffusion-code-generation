def is_leap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

assert is_leap(4) == True
assert is_leap(100) == False
assert is_leap(400) == True

if __name__ == '__main__':
    print(is_leap(2000))
    print(is_leap(1900))
    print(is_leap(2024))