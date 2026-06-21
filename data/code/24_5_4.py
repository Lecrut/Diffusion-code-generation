def check_leap(year: int) -> bool:
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

if __name__ == '__main__':
    print(check_leap(2000))
    print(check_leap(1900))
    print(check_leap(2024))
    print(check_leap(2023))