import calendar

def get_first_sunday_after_jan_1_2024():
    year = 2024
    month = 1
    day = 1
    base_date = calendar.weekday(year, month, day)
    target_weekday = calendar.SUNDAY
    if base_date == target_weekday:
        offset = 7
    else:
        offset = target_weekday - base_date
    target_day = day + offset
    result_date = calendar.date(year, month, target_day)
    return result_date

if __name__ == '__main__':
    result = get_first_sunday_after_jan_1_2024()
    print(result)