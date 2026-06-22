def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def days_in_month(month, leap_year):
    if month == 2:
        return 29 if leap_year else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30

def total_days_in_year(year):
    leap_year = is_leap_year(year)
    days = sum((days_in_month(month, leap_year) for month in range(1, 13)))
    return days
if __name__ == '__main__':
    print(total_days_in_year(2023))
    print(total_days_in_year(2024))