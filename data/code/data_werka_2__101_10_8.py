import calendar

def get_day_of_week(year, month, day):
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index]

if __name__ == '__main__':
    result = get_day_of_week(2023, 12, 25)
    print(result)