def days_remaining(year):
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return 29 if is_leap_year else 28

if __name__ == '__main__':
    year = 2023
    print(days_remaining(year))