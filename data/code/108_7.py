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
    print(f"Date: {year1}-{month1}-{day1}, Day: {result1}")
    year2 = 2023
    month2 = 2
    day2 = 29
    result2 = date_to_day(year2, month2, day2)
    print(f"Date: {year2}-{month2}-{day2}, Day: {result2}")
    year3 = 2024
    month3 = 3
    day3 = 31
    result3 = date_to_day(year3, month3, day3)
    print(f"Date: {year3}-{month3}-{day3}, Day: {result3}")
    year4 = 2023
    month4 = 12
    day4 = 31
    result4 = date_to_day(year4, month4, day4)
    print(f"Date: {year4}-{month4}-{day4}, Day: {result4}")
    year5 = 2024
    month5 = 2
    day5 = 28
    result5 = date_to_day(year5, month5, day5)
    print(f"Date: {year5}-{month5}-{day5}, Day: {result5}")