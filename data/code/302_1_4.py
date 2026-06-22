def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        raise ValueError('Invalid month')
if __name__ == '__main__':
    print(days_in_month(2020, 2))
    print(days_in_month(2019, 2))
    print(days_in_month(2023, 4))