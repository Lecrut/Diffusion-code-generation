import math
def day_of_week_first_of_month(year, month):
    if month == 1:
        h = 1
        d = 1
    else:
        h = 1
        d = month
    a = year % 100
    y = year // 100
    m = month
    k = (13 * (a % 4) + a) % 12
    j = a // 4
    k = (k + j) % 12
    h = (13 * (m + 1) + k + j - 1) % 7
    if h < 0:
        h += 7
    return h
if __name__ == '__main__':
    year1 = 2023
    month1 = 1
    result1 = day_of_week_first_of_month(year1, month1)
    print(f"Year: {year1}, Month: {month1}, Day of week for the 1st: {result1}")
    year2 = 2024
    month2 = 1
    result2 = day_of_week_first_of_month(year2, month2)
    print(f"Year: {year2}, Month: {month2}, Day of week for the 1st: {result2}")
    year3 = 2023
    month3 = 10
    result3 = day_of_week_first_of_month(year3, month3)
    print(f"Year: {year3}, Month: {month3}, Day of week for the 1st: {result3}")
    year4 = 2024
    month4 = 3
    result4 = day_of_week_first_of_month(year4, month4)
    print(f"Year: {year4}, Month: {month4}, Day of week for the 1st: {result4}")