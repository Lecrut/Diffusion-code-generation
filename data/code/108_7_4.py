import calendar
def day_of_month_manual(year, month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = False
    if year % 4 == 0:
        is_leap = True
    elif year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
    if is_leap:
        days_in_month[2] = 29
    if 1 <= month <= 12:
        return days_in_month[month]
    else:
        return -1
if __name__ == '__main__':
    year1 = 2024
    month1 = 31
    result1 = day_of_month_manual(year1, month1)
    print(f"Date: {year1}-{month1}, Day of Month: {result1}")
    year2 = 2000
    month2 = 2
    result2 = day_of_month_manual(year2, month2)
    print(f"Date: {year2}-{month2}, Day of Month: {result2}")
    year3 = 2023
    month3 = 12
    result3 = day_of_month_manual(year3, month3)
    print(f"Date: {year3}-{month3}, Day of Month: {result3}")
    year4 = 2024
    month4 = 2
    result4 = day_of_month_manual(year4, month4)
    print(f"Date: {year4}-{month4}, Day of Month: {result4}")