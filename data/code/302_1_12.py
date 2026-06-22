def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month < 1 or month > 12:
        raise ValueError('Invalid month')
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
if __name__ == '__main__':
    print(days_in_month(2020, 2))
    print(days_in_month(2019, 2))
    print(days_in_month(2021, 4))