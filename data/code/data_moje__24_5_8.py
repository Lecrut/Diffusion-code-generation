def check_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    print(check_leap(2000))
    print(check_leap(1900))
    print(check_leap(2024))
    print(check_leap(2023))