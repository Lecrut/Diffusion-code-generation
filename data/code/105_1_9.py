import calendar

def first_sunday_after_jan_1_2024():
    year = 2024
    month = 1
    day = 1
    weekday = calendar.weekday(year, month, day)
    if weekday == 6:
        return calendar.date(year, month, day)
    days_to_add = 6 - weekday
    result_day = day + days_to_add
    if result_day <= calendar.monthrange(year, month)[1]:
        return calendar.date(year, month, result_day)
    next_month = month + 1
    return calendar.date(year, next_month, 1)

if __name__ == '__main__':
    result = first_sunday_after_jan_1_2024()
    print(result)