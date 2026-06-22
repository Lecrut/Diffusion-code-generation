import calendar

def get_day_of_week(year, month, day):
    weekday_index = calendar.weekday(year, month, day)
    weekday_name = calendar.day_name[weekday_index]
    return weekday_name

if __name__ == '__main__':
    year = 2023
    month = 12
    day = 25
    result = get_day_of_week(year, month, day)
    print(result)