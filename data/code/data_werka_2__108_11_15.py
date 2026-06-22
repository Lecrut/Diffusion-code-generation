from datetime import date

def get_day_value(d):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    y = d.year
    m = d.month
    if m == 2:
        leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        max_d = 29 if leap else 28
    else:
        max_d = month_days[m - 1]
    if d.day > max_d:
        raise ValueError("Invalid day for given month")
    return d.day

if __name__ == '__main__':
    target = date(2023, 3, 15)
    day_num = get_day_value(target)
    print(day_num)