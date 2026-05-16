import calendar
def date_to_day(year, month, day):
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            max_days = 29
        else:
            max_days = 28
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 31
    if day > max_days:
        return None
    else:
        return day
if __name__ == '__main__':
    year1 = 2024
    month1 = 2
    day1 = 29
    result1 = date_to_day(year1, month1, day1)
    print(f"Date: {year1}-{month1}-{day1}, Day of Month: {result1}")
    year2 = 2023
    month2 = 1
    day2 = 31
    result2 = date_to_day(year2, month2, day2)
    print(f"Date: {year2}-{month2}-{day2}, Day of Month: {result2}")
    year3 = 2024
    month3 = 2
    day3 = 29
    result3 = date_to_day(year3, month3, day3)
    print(f"Date: {year3}-{month3}-{day3}, Day of Month: {result3}")
    year4 = 2023
    month4 = 2
    day4 = 29
    result4 = date_to_day(year4, month4, day4)
    print(f"Date: {year4}-{month4}-{day4}, Day of Month: {result4}")
    year5 = 2024
    month5 = 12
    day5 = 31
    result5 = date_to_day(year5, month5, day5)
    print(f"Date: {year5}-{month5}-{day5}, Day of Month: {result5}")