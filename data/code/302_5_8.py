def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def total_days_in_year(year):
    if is_leap_year(year):
        return 366
    else:
        return 365
if __name__ == '__main__':
    print(total_days_in_year(2020))
    print(total_days_in_year(2019))