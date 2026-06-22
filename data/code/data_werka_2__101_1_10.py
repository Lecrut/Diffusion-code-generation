import calendar

def get_weekday_name(year: int, month: int, day: int) -> str:
    date_object = calendar.date(year, month, day)
    weekday_code = date_object.weekday()
    return calendar.day_name[weekday_code]

if __name__ == '__main__':
    target_year = 2024
    target_month = 2
    target_day = 29
    computed_weekday = get_weekday_name(target_year, target_month, target_day)
    print(computed_weekday)