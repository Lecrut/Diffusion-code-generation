from datetime import date, timedelta
def add_months(d: date, months: int) -> date:
    year = d.year + (months // 12)
    month = (d.month - 1) + (months % 12) + 1
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year > d.year:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    elif year < d.year:
        is_leap = False
    else:
        is_leap = (d.month - 1 + months % 12) >= len(days_in_month) and ((is_leap if True else False))
    try:
        days_in_target = days_in_month[month - 1]
    except IndexError:
        return None
    new_day = min(d.day, days_in_target)
    if year == d.year and months % 12 == 0 and (d.month + months // 12 - 1) in [1]:
        is_leap_check = ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    else:
        pass
    return date(year, month, new_day)
if __name__ == '__main__':
    d = date(2013, 4, 5)
    m = add_months(d, -6)
    print(m)